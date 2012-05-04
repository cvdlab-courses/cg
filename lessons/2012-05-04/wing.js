// wing profile
var domain1 = INTERVALS(1)(30);
var domain2 = DOMAIN([[0,1],[0,1]])([15,30]);


var POLYPOINT = function (points) {
  return SIMPLICIAL_COMPLEX(points)(points.map(function (p,i) { 
    return [i];
  }));
}

var p0 = [[10,0,0],[0,5,0],[0,-3,0],[5,2,0],[10,0,0]];
var p1 = p0.map(function (p) {return [p[0], p[1], p[2]+10]});
var p2 = p0.map(function (p) {return [p[0], p[1]-1, p[2]+20]});
var p3 = p0.map(function (p) {return [p[0], p[1]+1, p[2]+30]});
var p4 = p0.map(function (p) {return [p[0], p[1], p[2]+40]});


var curvesPoints = STRUCT(AA(POLYPOINT)([p0,p1,p2,p3,p4]));
DRAW(curvesPoints);


var c0 = BEZIER(S0)(p0);
var c1 = BEZIER(S0)(p1);
var c2 = BEZIER(S0)(p2);
var c3 = BEZIER(S0)(p3);
var c4 = BEZIER(S0)(p4);
var controls = [c0,c1,c2,c3,c4]
// or 
var controls = AA(BEZIER(S0))([p0,p1,p2,p3,p4]);


var curves = STRUCT(CONS(AA(MAP)(controls))(domain1));

DRAW(curves);


var wing = BEZIER(S1)(controls);
var surf = MAP(wing)(domain2);
DRAW(surf);