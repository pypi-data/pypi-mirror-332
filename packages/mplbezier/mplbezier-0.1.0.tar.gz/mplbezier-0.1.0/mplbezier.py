import os
import pickle
import matplotlib as mpl
from matplotlib.path import Path
import matplotlib.patches as patches
from copy import deepcopy

CODES = [
    Path.MOVETO,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,
]


class Point:

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def set_d(self, dx, dy):
        self.dx = dx
        self.dy = dy


class Bezier:

    def __init__(self, ax, file, c='k', lw=1, ls='-'):
        self.ax = ax
        self.fig = self.ax.figure
        self.file = file

        self.color = c
        self.lw = lw
        self.ls = ls

        self.plot()
        self.picked = None
        self.anchor = None
        self.selected = None
        self.creating_point = False
        self.patches = []
        self.patch = None

        if os.path.exists(self.file):
            self.points = self.load()
        else:
            self.points = []

        self.point_history = [deepcopy(self.points)]
        self.update()

    def plot(self):
        self.anchorpoint_artist, = self.ax.plot([], [], visible=False,
                                                ls='', marker='o', picker=True,
                                                c='k', pickradius=10, markersize=4)
        self.anchorline_artist, = self.ax.plot([], [], visible=False,
                                               ls='-', marker='', picker=False,
                                               c='k', pickradius=10, lw=1)
        self.point_artist, = self.ax.plot([], [], visible=False,
                                          ls='', marker='s', picker=True,
                                          c='k', pickradius=10, fillstyle='none')

    def add_point(self, point):
        self.points.append(point)
        self.update()

    def set_anchor_data(self, xdata, ydata):
        self.anchorpoint_artist.set_data(xdata, ydata)
        self.anchorline_artist.set_data(xdata, ydata)

    def del_point(self, index):
        self.set_anchor_data([], [])
        del self.points[index]
        if len(self.points) > 0:
            self.patches[index - 1].remove()
            del self.patches[index - 1]
        self.picked = None
        self.update()
        self.fig.canvas.draw_idle()

    def update(self):
        x = [p.x for p in self.points]
        y = [p.y for p in self.points]
        self.point_artist.set_data(x, y)
        if len(self.points) > 1:
            for i in range(len(self.points) - 1):
                p1 = self.points[i]
                p2 = self.points[i + 1]
                verts = [
                    (p1.x, p1.y),
                    (p1.x + p1.dx, p1.y + p1.dy),
                    (p2.x - p2.dx, p2.y - p2.dy),
                    (p2.x, p2.y)
                ]
                path = Path(verts, CODES)
                if i < len(self.patches):
                    self.patches[i].set_path(path)
                else:
                    patch = patches.PathPatch(path, facecolor='none', lw=self.lw,
                                              ls=self.ls, edgecolor=self.color)
                    self.ax.add_patch(patch)
                    self.patches.append(patch)
        self.update_anchor()
        self.fig.canvas.draw_idle()
        self.save()

    def update_anchor(self):
        if self.selected is None:
            return
        p = self.points[self.selected]
        xdata = [p.x - p.dx, p.x + p.dx]
        ydata = [p.y - p.dy, p.y + p.dy]
        self.set_anchor_data(xdata, ydata)

    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        if self.picked is None and self.anchor is None:
            if event.button == 1:
                self.x, self.y = event.xdata, event.ydata
                self.add_point(Point(self.x, self.y, 0, 0))
                self.selected = len(self.points) - 1
                self.update()
                self.creating_point = True
            else:
                return
        if event.button == 3:
            self.selected = None
            self.del_point(self.picked)

    def on_release(self, event):
        self.picked = None
        if self.anchor is not None:
            self.anchor = None
        if self.creating_point:
            if event.inaxes == self.ax:
                x, y = event.xdata, event.ydata
                dx, dy = x - self.x, y - self.y
                self.points[-1].set_d(dx, dy)
            self.creating_point = False
        self.point_history.append(deepcopy(self.points))

    def on_pick(self, event):
        if event.artist is self.point_artist:
            self.event = event
            self.picked = event.ind[0]
            self.selected = self.picked
        if event.artist is self.anchorpoint_artist:
            self.anchor = event.ind[0]

        self.update()

    def on_motion(self, event):
        if event.inaxes != self.ax:
            return
        x, y = event.xdata, event.ydata
        if self.creating_point:
            dx, dy = x - self.x, y - self.y
            self.points[-1].set_d(dx, dy)
            self.update()
            return
        if self.anchor is not None:
            p = self.points[self.selected]
            if self.anchor == 1:
                dx, dy = x - p.x, y - p.y
            elif self.anchor == 0:
                dx, dy = p.x - x, p.y - y
            self.points[self.selected].set_d(dx, dy)
            self.update()
            return
        if self.picked is not None:
            self.points[self.picked].set_xy(x, y)
            self.update()

    def connect(self):
        self.events = []
        self.events.append(self.fig.canvas.mpl_connect('button_press_event', self.on_press))
        self.events.append(self.fig.canvas.mpl_connect('pick_event', self.on_pick))
        self.events.append(self.fig.canvas.mpl_connect('button_release_event', self.on_release))
        self.events.append(self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion))
        self.events.append(self.fig.canvas.mpl_connect("key_press_event", self.on_key))

    def disconnect(self):
        for event in self.events:
            self.fig.canvas.mpl_disconnect(event)

    def enable(self):
        self.connect()
        self.point_artist.set_visible(True)
        self.anchorline_artist.set_visible(True)
        self.anchorpoint_artist.set_visible(True)

    def disable(self):
        self.disconnect()
        self.point_artist.set_visible(False)
        self.anchorline_artist.set_visible(False)
        self.anchorpoint_artist.set_visible(False)

    def save(self):
        with open(self.file, 'wb') as file:
            return pickle.dump(self.points, file)

    def load(self):
        with open(self.file, 'rb') as file:
            return pickle.load(file)

    def on_key(self, event):
        if event.key == "ctrl+z" or event.key == "cmd+z":
            self.selected = None
            self.update_anchor()
            if len(self.point_history) > 1:
                for _ in range(len(self.points)):
                    self.del_point(0)
                self.point_history.pop()
                self.points = deepcopy(self.point_history[-1])
                self.update()