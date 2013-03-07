# Lesson 3
`07-03-2013`

## Requirements

* laptop

## Topics

* exercise review
* JavaScript crumbs
  - objects ([handbook](https://github.com/cvdlab/javascript-crumbs/blob/master/chapters/objects/Readme.md), [slides](http://apily.io/slidify?md=https://raw.github.com/cvdlab/javascript-crumbs-slides/master/chapters/objects/Readme.md))
  - functions ([handbook](https://github.com/cvdlab/javascript-crumbs/blob/master/chapters/functions/Readme.md), [slides](http://apily.io/slidify?md=https://raw.github.com/cvdlab/javascript-crumbs-slides/master/chapters/functions/Readme.md))
  

## Assignments

###exercise00a

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

### exercise00b

- create (or use an existing) personal repository named `learning-javascript`
- create `index.html` file into folder `<yyyy-mm-dd>`
- commit it and push it

### exercise01

write a script `exercise01.js` containing a function `identity(n)`  
that returns the `n` rows by `n` columns identity matrix

### exercise02

write a script `exercise02.js` containing a function `fibonacci(i)`   
that returns the i-th element of the Fibonacci's serie (apply memoization pattern)

### exercise03

write a script `exercise03.js` containing a constructor function for a 2DPoint object.  
A point should be described by its `x` and `y` coordinates.

### exercise04

write a script `exercise04.js` containing a contructor function for a Side object.  
a side should be described by its two vertices (i.e. two points).

### exercise05

write a script `exercise05.js` containing a constructor function for a Trinagle object.  
A triangle should be described by its three sides.  
A triangle object should be able to compute its own perimeter and area (do you remeber the Erone's formula?).


