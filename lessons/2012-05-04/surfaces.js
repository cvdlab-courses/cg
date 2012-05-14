// surfaces
var domain1 = INTERVALS(1)(30);
var domain2 = DOMAIN([[0,1],[0,1]])([15,30]);


var controls1 = [[1,0,0],[0,1,0],[0,2,0],[-2,0,0]]; // p0, p1, t0, t1
var c1 = CUBIC_HERMITE(S0)(controls1);
var curve1 = MAP(c1)(domain1);
// DRAW(curve1);


var controls2 = [[2,0,0],[0,2,0],[0,4,0],[-4,0,0]]; // p0, p1, t0, t1
var c2 = CUBIC_HERMITE(S0)(controls2);
var curve2 = MAP(c2)(domain1);
// DRAW(curve2);


var s12b = BEZIER(S1)([c1,c2]);
var surface12b = MAP(s12b)(domain2);
// DRAW(surface12b);
// DRAW(SKELETON(1)(surface12b));


var s12h = CUBIC_HERMITE(S1)([c1,c2,[0,0,3],[0,0,-3]]);
var surface12h = MAP(s12h)(domain2);
// DRAW(surface12h);

DRAW(STRUCT([curve1,curve2,surface12b,surface12h]));