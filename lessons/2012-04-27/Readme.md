# Practice 27/04

## Exercise 0
download `plasm.js` in your local machine  
write your code in `test/test.js` and open `test/index.html`

## Exercise 1
#### `POLYLINE`, `EXTRUDE`, `COLOR`

draw the plant of the following labyrint using `POLYLINE`  
raise the walls using `EXTRUDE`  
colors the walls using `COLOR`

```
    0 1 2 3 4 5 6 7 8 9
    | | | | | | | | | |
0 _  _________________
1 _ |  _____   _____  |
2 _ | |     | |     | |
3 _ |_|     |_|     |_|
4 _  _       _       _
5 _ | |     | |     | |
6 _ | |_____| |_____| |
7 _ |_________________|
```

## Exercise 2
#### `CUBOID`, `BOUNDARY`, `COLOR`

build the roof of the labyrint using `CUBOID`  
extract the surface of the roof using `BOUNDARY`  
color the surface of the roof as a glass using `COLOR`

## Exercise 3
###`CUBIC_HERMITE`

draw a cubical hermite curve with the following control points:

```
C(0):  (1,0)
C(1):  (1,1)
C'(0): (1,0)
C'(1): (1,1)
```

## Exercise 4
#### `BEZIER`

draw a bezier curve of degree 4 with following control points:  

```
P(0): (0,0)
P(1): (3,1)
P(2): (1,2)
P(3): (2,3)
P(4): (3,2)
```

## Exercise 5
#### `CUBIC_CARDINAL`, `SPLINE`

draw a cubic cardinal spline with following control points:

```
P(0): (-3,6)
P(1): (-4,2)
P(2): (-3,-1)
P(3): (-1,1)
P(4): (1.5,1.5)
P(5): (3,4)
P(6): (5,5)
P(7): (7,2)
P(8): (6,-2)
P(9): (2,-3)
```

## Exercise 6
#### `CUBIC_UBSPLINE`, `SPLINE`

Draw a cubic uniform b-spline with following control points:

```
P(0): (-3,6)
P(1): (-4,2) 
P(2): (-3,-1)
P(3): (-1,1)
P(4): (1.5,1.5)
P(5): (3,4)
P(6): (5,5)
P(7): (7,2)
P(8): (6,-2)
P(9): (2,-3)
```

## Exercise 7
#### `CUBIC_CARDINAL`, `CUBIC_UBSPLINE`, `SPLINE`, `SIMPLICIAL_COMPLEX`

Draw curves of exercises 5 and 6 in different color,  
displying control points too.


## Exercise 8

for each curve type, create a function drawing:  

- control points  
- a polyline joining controlpoints  
- generated curve  
