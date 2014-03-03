# 2013-03-25

## Requirements

* laptop

## Topics

* exercise review
* [Plasm.js](http://cvdlab.github.com/plasm.js/) introduction
* Plasm.js crumbs
  - introduction ([slides](http://apily.io/slidify?md=https://raw.github.com/cvdlab/plasm-crumbs-slides/master/chapters/introduction/Readme.md))
  - basics ([slides](http://apily.io/slidify?md=https://raw.github.com/cvdlab/plasm-crumbs-slides/master/chapters/basics/Readme.md))
      - `CUBE`
      - `DRAW`
      - `HIDE`
      - `SHOW`
      - `CUBOID`
      - `SIMPLEX`
      - `CYL_SURFACE`
      - `SIMPLEX_GRID`
      - `POLYLINE`
      - `SIMPLICIAL_COMPLEX`
  - transformations ([slides](http://apily.io/slidify?md=https://raw.github.com/cvdlab/plasm-crumbs-slides/master/chapters/transformations/Readme.md))
      - `T`
      - `R`
      - `S`
      - `STRUCT`
      - `EXTRUDE`
      - `COLOR`

## Code snippets

```js
var n = 20;
var l = 1;
var h = l/8;
var alpha = PI/12;
var brick = T([0,1])([-l/2,-l/2])(CUBOID([l,l,h]));
var rotation = R([0,1])([alpha]);
var traslation = T([2])([h]);
var models = REPLICA(n)([brick,rotation, traslation]);
var stack = STRUCT(models);
```

```js
DRAW(SIMPLEX_GRID(REPEAT(3)(REPLICA(16)([1,-0.5]))));
```

## Assignments

### exercise01

Try to model a simple house.
