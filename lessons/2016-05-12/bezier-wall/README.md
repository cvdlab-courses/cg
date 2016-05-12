# easy generation of curved walls

Below you may find an useful hint for the modeling of curved walls for your architectural project.

In particular you may model such artifact by providing a Bezier curve, the ortogonal width, and the wall hight. See belw:

```{.python}
from pyplasm import *

vertices=[[0,0],[1.5,0],[-1,2],[2,2],[2,0]]
VIEW(PROD([ BEZIERSTRIPE([vertices,0.15, 22]), QUOTE([.9,-.45,.45]) ]))
```
or
```
wallPlan = BEZIERSTRIPE([vertices,0.15, 22])
wall = PROD([ BEZIERSTRIPE([vertices,0.15, 22]), QUOTE([.9,-.45,.45]) ])
VIEW(STRUCT([wall,S(1)(-1),wall]))
```
Tha generated models are the following:

![single wall](wall.png | width=200)
![single wall](wall2.png | width=200)