/** es 1 **/

var domain = DOMAIN([[0,1]])([10]);
var mapping = function (v) {
  return [v[0],v[0]];
};

var model0 = MAP(mapping)(domain);

DRAW(model0);

/** es 2 **/

var domain = DOMAIN([[0,1]])([10]);

var x = function (v) {
  return [v[0]];
};

var y = function (v) {
  return [v[0]];
};

var z = function (v) {
  return [v[0]];
}

var mappings = [x,y,z];

var model1 = MAP(mappings)(domain);

DRAW(model1);

/** es 3 **/

var domain = DOMAIN([[0,2*PI]])([36]);

var x = function (v) {
  return [v[0]];
};

var y = function (v) {
  return [SIN(v[0])];
}

var mappings = [x,y];

var model = MAP(mappings)(domain);

DRAW(model);

/** es 4 **/

var domain1 = DOMAIN([[0,2*PI]])([36]);
var domain2 = DOMAIN([[0,8*PI]])([36]);
var domain3 = DOMAIN([[0,8*PI]])([120]);

var x = function (v) {
  return [v[0]];
};

var y = function (v) {
  return [SIN(v[0])];
}

var mappings = [x,y];

var map = MAP(mappings);

var model1 = map(domain1);
var model2 = map(domain2);
var model3 = map(domain3);

DRAW(model1);
DRAW(model2);
DRAW(model3);

/** es 5 **/

var domain = DOMAIN([[0,2*PI]])([36]);

var mapping = function (v) {
  return [COS(v[0]), SIN(v[0])];
};

var model = MAP(mapping)(domain);

DRAW(model);

/** es 6 **/

var domain = DOMAIN([[0,2*PI]])([36]);
var r = 2;

var mapping = function (v) {
  return [r*COS(v[0]), r*SIN(v[0])];
};

var model = MAP(mapping)(domain);

DRAW(model);

/** es 7 **/

var domain = DOMAIN([[0,2*PI]])([36]);

var circle = function (r) {
  return function (v) {
    return [r*COS(v[0]), r*SIN(v[0])];
  };
};

var mapping = circle(3);

var model = MAP(mapping)(domain);

DRAW(model);

/** es 8 **/

var domain = DOMAIN([[0,PI],[0,2*PI]])([24,36]);

var mapping = function (v) {
  var a = v[0];
  var b = v[1];

  var u = SIN(a) * COS(b);
  var v = SIN(a) * SIN(b);
  var w = COS(a);

  return [u,v,w];
};

var model = MAP(mapping)(domain);

DRAW(model);

/** es 9 **/

var domain = DOMAIN([[0,2*PI],[0,2*PI]])([36,72]);

var torus = function (R, r) {
  return function (v) {
    var a = v[0];
    var b = v[1];

    var u = (r * COS(a) + R) * COS(b);
    var v = (r * COS(a) + R) * SIN(b);
    var w = (r * SIN(a));

    return [u,v,w];
  }
}

var mapping = torus(3,1);

var model = MAP(mapping)(domain);

DRAW(model);
