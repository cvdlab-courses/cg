// nubs
var domain1 = INTERVALS(1)(15);
var domain2 = DOMAIN([[0,1],[0,1]])([15,30]);

var controls1 = [[0,0,0],[2,5,0],[7,3,0],[9,7,0],[12,2,0]];
var knots1 = [0,0,0,1,2,3,3,3];
var c1 = NUBS(S0)(2)(knots1)(controls1);
var curve1 = MAP(c1)(domain1);
DRAW(curve1);


var controls2 = [[0,0,0],[2,5,3],[7,3,6],[9,7,-2],[12,2,-3]];
var knots2 = [0,0,0,1,2,3,3,3];
var c2 = NUBS(S0)(2)(knots2)(controls2);
var curve2 = MAP(c2)(domain1);
DRAW(curve2);


var s12 = BEZIER(S1)([c1,c2]);
var surf = MAP(s12)(domain2);
DRAW(surf);




