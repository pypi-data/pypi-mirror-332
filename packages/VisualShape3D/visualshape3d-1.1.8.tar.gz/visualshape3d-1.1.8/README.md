# Project Overview
VisualShape3D is such a Python library that is meant to easily create 3D polygons for modeling physics in classroom.
## About VisualShape3D
### Shape Creation
2D Polygon Generation :    

Initially, a polygon is defined in the YZ plane with its first vertice located at the orign of XYZ system and its facet in the direction of X. 
```Python
from VisualShape3D.Shape3D import Shape

shape1 = Shape('rectangle', W, H)
shape2 = Shape('triangle', W, H, A)
shape3 = Shape('rectangleWithHole', W, H, A, B, C, D)
shape4 = Shape('fourSided', W, H, A, B)
shape5 = Shape('fiveSided', W, H, A, B, C, D)
shape6 = Shape('regularPolygon', n, R)
shape7 = Shape('polygon', [(x1, y1), (x2, y2), ..., (xn, yn)])
```
In the YZ plane, these polygon are 2D, and easily, their vertices are generated given its dimensions.

### Transformation
For a created polygon, it can move from (0,0,0) to (X, Y, Z) with regards to its origin, and its orientation of facet in the X direction can turn to others by anticlockwise rotation $alpha$ about a line in parallel to the Z axis that is passing through the first vertice, and clockwise rotation of $beta$ about its horizontal bottom edge. 

#### The way to do them
```Python
shape1 = shape1.transform(to=(X, Y, Z))
shape1 = shape1.transform(alpha=alpha1)
shape1 = shape1.transform(beta=beta1)
```

#### Or the compact way 
```Python
shape1 = shape1.transform(to=(X, Y, Z), angles=(alpha1, beta1))
```

### Reference point
By default, the first vertex of polygon serves for the reference point of translation, but one can choose other one of the polygon by argument 'reference='.

### Visualization
Built - on Matplotlib:
Visualize the results within the VisualShape3D framework, which is built on Matplotlib.

```Python
from VisualShape3D.Visual import VisualShape3D

vs3d = VisualShape3D()
vs3d.add_shape(shape1)
vs3d.show()
```

# A complete example 

## to list all shapes of polygons in the package that are ready for use :
```Python
import VisualShape3D.shapes as sp
sp.shapes()
```

## To show how to use the package

### To Create shapes
```Python
from VisualShape3D.Shape3D import Shape 
W, H = 1, 0.7
shape1 = Shape('rectangle', W, H)
shape2 = shape1.transform(alpha = 30)
shape3 = shape2.transform(beta = 30)
shape4 = shape3.transform(to=(-0.5,-0.5,0))
```

### To show them all

```Python
from VisualShape3D import Visual as vm 
visual = vm.VisualShape3D({'facecolor':'yellow','alpha':0.7})
visual.add_shape(shape1,{'facecolor':'slategrey','alpha':0.7})
visual.add_shape(shape2,{'facecolor':'slategrey','alpha':0.7})
visual.add_shape(shape3,{'facecolor':'slategrey','alpha':0.7})
visual.add_shape(shape4,{'facecolor':'slategrey','alpha':0.7})
visual.show()
```


# Core Features

## Translation
Moves the reference point of the shape to a new 3D position.   
## Rotation
Adjusts the facets of the shape to a new direction about the Z - axis. The first vertex serves as the pivot point for these transformations, including rotation around the first edge. These operations are independent of each other.
## Visualization
Show the result of modeling at all once.

# Requirements
Python 3 is required, and Matplotlib must be installed.

# Installation
You can easily install VisualShape3D using pip:
pip install VisualShape3D


# Update Log
Version 1.1.8. Improvement of projection description.  
Version 1.1.7: Renamed VisualShape3D.shapes to VisualShape3D.Polygons
Version 1.1.6: Renamed VisualShape3D.geometry to VisualShape3D.Shape3D and VisualShape3D.VisualModels to VisualShape3D.Visual.
Version 1.0.7: Fixed the bug of Shape_rectangleWithHole.
Version 1.0.6: Changed the description about VisualShape3D.
Version 1.0.5: Added "Modeling a house with shape" and "Building model" jupyter files.

# Documentation
Documentation is still in progress. Stay tuned for more detailed guides on using VisualShape3D.
