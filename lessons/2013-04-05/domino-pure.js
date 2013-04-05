foundations = SIMPLEX_GRID([[8,-30,8,-30,8,-12,8],[8,-30,8],[6]])
// DRAW(foundations)



pillars = SIMPLEX_GRID([[-3,2,-36,2,-36,2,-18,2],[-3,2,-36,2],[-7.4,23.6,-1.4,23.6,-1.4]])
building = STRUCT([foundations,pillars])
// DRAW(building)



beams_x = SIMPLEX_GRID([[-3,2,36,2,36,2,18,2],[-3,2,-36,2],[-6,1.4,-23.6,1.4,-23.6,1.4]])
beams_y = SIMPLEX_GRID([[-3,2,-36,2,-36,2,-18,2],[-3,2,36,2],[-6,1.4,-23.6,1.4,-23.6,1.4]])
beams = STRUCT([beams_x,beams_y])
frame = STRUCT([foundations,pillars,beams])
// DRAW(frame)



horiz_partitions = T([1])([-6])(SIMPLEX_GRID([[-1,2,2,36,2,36,2,18,2,2],[9,2,36,2,9],[-6,1.4,-23.6,1.4,-23.6,1.4]]))
frame = STRUCT([foundations,pillars])
building = STRUCT([frame, horiz_partitions])
// DRAW(building)



hpartition1 = SIMPLEX_GRID([[-1,2,2,36,2,36,2,-18,2,2],[9,2,12,24,2,9],[-6,1.4,-23.6,1.4,-23.6,1.4]])
hpartition2 = SIMPLEX_GRID([[-1-2-2-36-2-36-2,18],[9,2,12,-24,-9,2],[-6,1.4,-23.6,1.4,-23.6,1.4]])
hpartition3 = SIMPLEX_GRID([[-1-2-2-36-2-36-2,18],[9,2,12,24,2,9],[-6,1.4,-23.6,-1.4,-23.6,1.4]])
hpartition4 = SIMPLEX_GRID([[-1-2-2-36-2-36-2,18],[-9,-2,-12,-24,9],[-6,1.4,-25/2. +1.4,1.4]])
horiz_partitions = STRUCT([ hpartition1, hpartition2, hpartition3, hpartition4 ])
building = STRUCT([frame, horiz_partitions])
// DRAW(building)



depth = 2.66
raiser = 25.0/(2*9)
step2D = SIMPLICIAL_COMPLEX([[0,0],[0,1.4+raiser],[depth,raiser],[depth,1.4+raiser]])([[0,2,1],[1,2,3]])
step3D = MAP([S0,S2,S1])(EXTRUDE([9])(step2D));
ramp = STRUCT(REPLICA(9)([step3D,T([0,2])([depth,raiser])]))
// DRAW(ramp)



ramp1 = T([0,1,2])([3+2+36+2+36+2+18,3+2+12,6])(R([0,1])(PI/2)(ramp))
ramp2 = T([0,1,2])([3+2+36+2+36+2,3+2+12+24,6+25/2.])(R([0,1])(-PI/2)(ramp))
stair = STRUCT([ramp1,ramp2])
// DRAW(stair)



building = STRUCT([foundations,pillars,T([1])([-6])(horiz_partitions),stair])
// DRAW(building)



enclosure_north = COLOR([1,0,0])(SIMPLEX_GRID([[-1,2,2,36,2,36,2,18,2,2],[-5,-2,-12,-24,-7,2], [-6,-1.4,23.6,-1.4,23.6,-1.4]]))
enclosure_south = COLOR([0,1,0])(SIMPLEX_GRID([[-1,2+2+36+2+36+2+18+2+2],[2], [-6,-1.4,23.6,-1.4,23.6,-1.4]]))
enclosure_west = COLOR([0,0,1])(SIMPLEX_GRID([[-1,2],[-2,4,2,36,2,4,6],[-6,-1.4,23.6,-1.4,23.6,-1.4]]))
    
building = STRUCT([foundations,pillars,T([1])([-6])(horiz_partitions),ramp1,ramp2,enclosure_north,T([1])([-6])(enclosure_south),T([1])([-6])(enclosure_west)])    
// DRAW(building)



wall01 = COLOR([0,1,1])(T([0,1])([3+2+36+2+36+1, 3+2+12])(SIMPLEX_GRID([[1],[24,-2,7],[-6,-1.4,23.6,-1.4,23.6]])))
building = STRUCT([foundations,pillars,T([1])([-6])(horiz_partitions),ramp1,ramp2, enclosure_north,T([1])([-6])(enclosure_south),T([1])([-6])(enclosure_west), wall01])
DRAW(building)

