var pillars = SIMPLEX_GRID([
  REPLICA(3)([0.15,-6*2.4,0.15]),
  [0.15,-6*2.4,0.15],
  [1.5,3,3]
]);

var beams = SIMPLEX_GRID([
  REPLICA(3)([0.15,-6*2.4,0.15]),
  [14.7],
  [-7.5,1.5]
]);

var steelFrames = COLOR([0.2,0.2,0.2])(STRUCT([pillars,beams]));

var floors = SIMPLEX_GRID([
  REPLICA(3)(14.7),
  [-0.15,14.4,-0.15],
  [-1.2,0.3,-2.7,0.3,-2.7,0.3]
]);

var cantileverFloor = SIMPLEX_GRID([
  [0.15,2*2.4,0.15],
  [-0.15,14.4,-0.15],
  [-1.2,0.3,-2.7,0.3,-2.7,0.3]
]);

var cantileverPillars = SIMPLEX_GRID([
  [0.15],
  [0.15,-14.4,0.15],
  [1.5,3,3]
]);

var cantileverBeams = SIMPLEX_GRID([
  [0.15],
  [14.7],
  [-7.5,1.5]
]);

var cantileverSteelFrames = COLOR([0.2,0.2,0.2])(STRUCT([cantileverPillars,cantileverBeams]));

var cantilever = STRUCT([cantileverFloor,cantileverSteelFrames]);

var cantilever1 = S([0])([-1])(cantilever);
var cantilever2 = T([0])([3*14.7])(cantilever);

var grid1 = SIMPLEX_GRID([ [-0.15, 0.05, -2.3, 0.05], [0.15], [1.5,3,3] ]);
var grid2 = SIMPLEX_GRID([ [-0.15, -0.05, 2.3, -0.05], [0.15], [0.3, -0.9, 0.3,-2.95,0.05,-2.7,0.3] ]);
var grid3 = SIMPLEX_GRID([ [-0.15, -0.05, -1.125, 0.05, -1.125,  -0.05], [0.15], [-0.3, 0.9, -0.3, 2.95,0.05] ]);
var panel = SIMPLEX_GRID([ [-0.15, -0.05, 1.125, -0.05, 1.125,  -0.05], [-0.1,0.05], [-0.3, 0.9, -0.3, 2.95/2] ]);

var grid = COLOR([0.2,0.2,0.2])(STRUCT([grid1,grid2,grid3]));
var frame = function(color) {return STRUCT([ COLOR(color)(panel), grid])};
var frameGroup = function(number,color) {return STRUCT( REPLICA(number)([ frame(color), T([0])([2.4]) ]))};

var colors = [[1,0,0],[0,1,0],[0,0,1],[0,1,1],[1,0,1],[1,1,0]];
var frames = STRUCT([
  frameGroup(3,colors[0]), T([0])([3*2.4]),
  frameGroup(3,colors[1]), T([0])([3*2.4]), T([0])([0.3]),
  frameGroup(3,colors[2]), T([0])([3*2.4]),
  frameGroup(3,colors[3]), T([0])([3*2.4]), T([0])([0.3]),
  frameGroup(3,colors[4]), T([0])([3*2.4]),
  frameGroup(3,colors[5])
]);

var backFrames = T([1])([14.7])(S([1])([-1])(frames));

DRAW(STRUCT([ steelFrames,floors,cantilever1,cantilever2,frames,backFrames ]));

