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
