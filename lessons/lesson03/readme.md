# Lesson 3
`07-03-2013`

## Requirements

* laptop

## Topics

* exercise review
* JavaScript crumbs
  - functions ([handbook](https://github.com/cvdlab/javascript-crumbs/blob/master/chapters/functions/Readme.md), [slides](https://github.com/cvdlab/javascript-crumbs-slides/blob/master/chapters/functions/Readme.md))
  - objects ([handbook](https://github.com/cvdlab/javascript-crumbs/blob/master/chapters/objects/Readme.md), [slides](https://github.com/cvdlab/javascript-crumbs-slides/blob/master/chapters/objects/Readme.md))

## Assignments

###exercise00

try to understand what happens in here:

```js
function greets () {
 console.log('Hello!');
 greets = function () {
   console.log('Bye!');
   return greets;
 };
 return greets;
}

greets();

greets()();

greets()()();
```

```js
function greets () {
 console.log('Hello!');
 var greets = function () {
   console.log('Bye!');
   return greets;
 };
 return greets;
}

greets();

greets()();

greets()()();
```

### exercise01

define a function that returns the `n` rows by `n` columns identity matrix

### exercise02

define a constructor function to create a 2DPoint object.  
A point should be described by its x and y coordinates.

### exercise03

define a constructor function to create a Trinagle object.
A triangle should be described by its vertices, which are points.


