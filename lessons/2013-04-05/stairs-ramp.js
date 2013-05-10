// stairs ramp 

var depth = 2.66;
var raiser = 25.0/(2*9);
var step2D = SIMPLICIAL_COMPLEX([[0,0],[0,1.4+raiser],[depth,raiser],[depth,1.4+raiser]])([[0,2,1],[1,2,3]]);
var step3D = MAP([S0,S2,S1])(EXTRUDE([9])(step2D));
var ramp = STRUCT(REPLICA(9)([step3D,T([0,2])([depth,raiser])]));

DRAW(ramp);