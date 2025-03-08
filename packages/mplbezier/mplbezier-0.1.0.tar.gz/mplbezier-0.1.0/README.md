# mplbezier

This module allows you to draw Bezier curves interactively in matplotlib and load them again afterwards. Install it by
cloning the git repository, navigating into the repository root directory and typing into the console:

```console
pip install .
```

Simply import `Bezier` from `mplbezier` and create a new `Bezier` object, which you pass both the `Axis` and a filename 
of a `pickle` file to store the anchor point data. Using `Bezier.enable`, you enable the interactive drawing mode. In 
order to use the interactive drawing mode, you need to be inside an interactive matplotlib backend, such as `qtagg`.
If you are using this module from a Jupyter notebook, switch to interactive mode using magic commands such as 
`%matplotlib Qt` at the top of the cell.

```python
import matplotlib.pyplot as plt
from mplbezier import Bezier

fig, ax = plt.subplots()

b = Bezier(ax, 'my_curve.pkl')
b.enable()

plt.show()
```

By clicking with the left mouse button inside the plot, you will generate a new anchor point. By clicking on an anchor
point, you can reveal the handles with which you can define the position of the control points. By dragging a point, you 
can move it on the axis. By right clicking a point, you can remove it from the Bezier curve. If the point lies between
two other points, the curve will automatically connect the two surrounding points with each other. Moreover, "ctrl+z" is
supported to undo your last action.

Once you are satisfied with your curve, you can remove or comment out the line `b.enable()`. This will remove the
anchor points from the curve, thereby giving you the final plot.

The curve can be initialized with three keyword arguments:
- `c` sets the color (default 'black')
- `lw` sets the linewidth (default 1)
- `ls` sets the linestyle (default ('-')

![img.png](example.png)