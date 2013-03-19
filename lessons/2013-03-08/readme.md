# 2013-03-08

### Requirements:

* laptop

## Arguments

* exercise review
* JavaScript crumbs
  - Built-in objects ([handbook](https://github.com/cvdlab/javascript-crumbs/blob/master/chapters/built-in/Readme.md), [slides](http://apily.io/slidify?md=https://raw.github.com/cvdlab/javascript-crumbs-slides/master/chapters/built-ins/Readme.md))
      - Array
      - String
      - Number
      - Math
      - Date
      - RegExp

### Assignments
push your exercises in a folder named `<yyyy-mm-dd>`, as usual

### exercise01

#### exercise01a

write a function that pushes into an array the first `n` natural numbers

#### exercise01b

filter out odd number and return the even ones

#### exercise01c

double each even number obtained

#### exercise01d

return only numbers divisible by four

#### exercise01e

sum all the remaining numbers

### exercise02

#### exercise02a

write a function that pushes into an array `n` random integer numbers

#### exercise02b

filter even numbers and return the odd ones

#### exercise02c

sort obtained numbers from the smallest to the largest


### exercise03

#### exercise03a

write a function that given a word return it capitalized

#### exercise03b

write a function that capitalize each word of the following text:

```
"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
```

### exercise04

write a function `select(data, key, values)` that given an array of objects `data`, a string `key` and an array of values `values`, returns the array of objects where the property `key` is equal to one of the values in `values`. For example:

```js
var data = [
  {id:'01', name:'duffy'},
  {id:'02', name:'michey'},
  {id:'03', name:'donald'},
  {id:'04', name:'goofy'},
  {id:'05', name:'minnie'},
  {id:'06', name:'scrooge'}
];
var key = 'name';
var values = ['goofy', 'scrooge'];

select(data, key, values)
// [ { id:'04', name:'goofy' }, { id:'06', name:'scrooge' } ]
```
