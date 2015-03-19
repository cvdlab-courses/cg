var range = function (n) {
  var result = [];
  while (--n) {
    result.unshift(n);
  }
  return result;
};

var even = function (item) {
  return item % 2 === 0;
};

var double = function (item) {
  return item * 2;
};

var divisible_by_4 = function (item) {
  return item % 4 === 0;
};

var sum = function (prev, curr) {
  return prev + curr;
};

var n = 10;
var result = range(n)
  .filter(even)
  .map(double)
  .filter(divisible_by_4)
  .reduce(sum);

console.log(result);
