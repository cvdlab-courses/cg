from pyplasm import *

house = POLYLINE([[0,0],[5,0],[5,5],[2.5,7],[0,5],[0,0]])

points = [[0,0],[5,0],[5,5],[2.5,7],[0,5],[0,0]]
cells = [[1,2,3,4,5]]
wall = MKPOL([points,cells,None])

door = T(1)(2)(COLOR(CYAN)(CUBOID([1,3])))
window = T([1,2])([3.5,1])(COLOR(MAGENTA)(CUBOID([0.75,2])))

house_1 = SKELETON(1)(STRUCT([wall,door,window]))
bell_tower = S([1,2])([.5,2])(SKELETON(1)(wall))

church = STRUCT([house_1,T(1)(-2.5)(bell_tower)])
church_1 = S(2)(-1)(church)

VIEW(STRUCT([house_1,S(1)(-1)(house_1)]))

VIEW(R([1,2])(PI/18)(church))

def shear(a): return MAT([[1,0,0],[0,1,a],[0,0,1]])
VIEW(shear(1/3.)(house_1))