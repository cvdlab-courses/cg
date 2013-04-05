# Maison Domino


from pyplasm import *
GRID = COMP([INSR(PROD),AA(QUOTE)])



foundations = GRID([[8,-30,8,-30,8,-12,8],[8,-30,8],[6]])
VIEW(foundations)


pillars = GRID([[-3,2,-36,2,-36,2,-18,2],[-3,2,-36,2],
    [-7.4,23.6,-1.4,23.6,-1.4]])
building = STRUCT([foundations,pillars])
VIEW(building)



beams_x = GRID([[-3,2,36,2,36,2,18,2],[-3,2,-36,2],
    [-6,1.4,-23.6,1.4,-23.6,1.4]])
beams_y = GRID([[-3,2,-36,2,-36,2,-18,2],[-3,2,36,2],
    [-6,1.4,-23.6,1.4,-23.6,1.4]])
beams = STRUCT([beams_x,beams_y])
frame = STRUCT([foundations,pillars,beams])
VIEW(frame)



horiz_partitions = T(2)(-6)(GRID([[-1,2,2,36,2,36,2,18,2,2],
    [9,2,36,2,9],[-6,1.4,-23.6,1.4,-23.6,1.4]]))
frame = STRUCT([foundations,pillars])
building = STRUCT([frame, horiz_partitions])
VIEW(building)



hollow = T([1,2,3])([5+38*2, 5+12, 6+25])(CUBOID([18,33,1.4]))
horiz_partitions = DIFFERENCE([ horiz_partitions, hollow])
building = STRUCT([frame,horiz_partitions])
VIEW(building)



hpartition1 = GRID([[-1,2,2,36,2,36,2,-18,2,2],[9,2,12,24,2,9],
    [-6,1.4,-23.6,1.4,-23.6,1.4]])
hpartition2 = GRID([[-1-2-2-36-2-36-2,18],[9,2,12,-24,-9,2],
    [-6,1.4,-23.6,1.4,-23.6,1.4]])
hpartition3 = GRID([[-1-2-2-36-2-36-2,18],[9,2,12,24,2,9],
    [-6,1.4,-23.6,-1.4,-23.6,1.4]])
hpartition4 = GRID([[-1-2-2-36-2-36-2,18],[-9,-2,-12,-24,9],
    [-6,1.4,-25/2. +1.4,1.4]])
horiz_partitions = STRUCT([ hpartition1, hpartition2, 
    hpartition3, hpartition4 ])
building = STRUCT([frame, horiz_partitions])
VIEW(building)



depth = 2.66 # pedata 
raiser = 25.0/(2*9) # alzata
step2D = MKPOL([[[0,0],[0,1.4+raiser],[depth,raiser],[depth,1.4+raiser]],
    [[1,2,3,4]],None])
step3D = MAP([S1,S3,S2])(PROD([step2D,Q(9)]))
ramp = STRUCT(NN(9)([step3D,T([1,3])([depth,raiser])]))
VIEW(ramp)



ramp1 = T([1,2,3])([3+2+36+2+36+2+18,3+2+12,6])(R([1,2])(PI/2)(ramp))
ramp2 = T([1,2,3])([3+2+36+2+36+2,3+2+12+24,6+25/2.])(
    R([1,2])(-PI/2)(ramp))
stair = STRUCT([ramp1,ramp2])
VIEW(stair)



building = STRUCT([foundations,pillars,T(2)(-6)(horiz_partitions),stair])
VIEW(building)



enclosure_north = COLOR(RED)(GRID([[-1,2,2,36,2,36,2,18,2,2], 
    [-5,-2,-12,-24,-7,2], [-6,-1.4,23.6,-1.4,23.6,-1.4]]))
    
enclosure_south = COLOR(GREEN)(GRID([[-1,2+2+36+2+36+2+18+2+2],
    [2], [-6,-1.4,23.6,-1.4,23.6,-1.4]]))
    
enclosure_west = COLOR(BLUE)(GRID([[-1,2],[-2,4,2,36,2,4,6],
    [-6,-1.4,23.6,-1.4,23.6,-1.4]]))
    
building = STRUCT([foundations,pillars,T(2)(-6)(horiz_partitions),
    ramp1,ramp2,enclosure_north,
    T(2)(-6)(enclosure_south),T(2)(-6)(enclosure_west)])
    
VIEW(building)




wall01 = COLOR(YELLOW)(T([1,2])([3+2+36+2+36+1, 3+2+12])(
    GRID([[1],[24,-2,7],[-6,-1.4,23.6,-1.4,23.6]])))
building = STRUCT([foundations,pillars,T(2)(-6)(horiz_partitions),
    ramp1,ramp2, enclosure_north,T(2)(-6)(enclosure_south),
    T(2)(-6)(enclosure_west), wall01])
VIEW(building)


