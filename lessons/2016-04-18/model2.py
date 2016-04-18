from larlib import *

""" duplex apartment -- first draft """

lines = lines2lines("up-level.lines")
upLevel = STRUCT(AA(POLYLINE)(lines))
VIEW(upLevel)
VIEW(OFFSET([.005,.005])(upLevel))
VIEW(SKEL_1(OFFSET([.005,.005])(upLevel)))

V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

larUpLevel1D = V,EV

thinWalls = sorted([30,61,29,  43,32,15,8,48,33,28,9,0,24,39,67,35,55,
21,63,57,46,17, 51,25,65, 2,20,49,13, 11,41,44, 71,18,47,10, 53,26, 14,31])
thickWalls = set(range(len(EV))).difference(thinWalls)
thinHPCs = STRUCT(AA(POLYLINE)([[V[EV[e][0]],V[EV[e][1]]] for e in thinWalls]))
thickHPCs = STRUCT(AA(POLYLINE)([[V[EV[e][0]],V[EV[e][1]]] for e in thickWalls]))
thin = COLOR(YELLOW)(OFFSET([.0025,.0025])(thinHPCs))
thick = COLOR(CYAN)(OFFSET([.005,.005])(thickHPCs))
VIEW(STRUCT([ thin, thick ]))
VIEW(PROD([ STRUCT([thin,thick]), INTERVALS(3./24)(1) ]))

""" Adjustment of building width """

L1,L2 = lines2lines("duplex-width.lines")  # ERROR, bug
xbalcony = 70./1022.*24.00
xbasament = 24.0 - 2*xbalcony
assert xbasament == 20.71232876712329

""" mid floor of duplex  """

lines = lines2lines("mid-level.lines")
upLevel = STRUCT(AA(POLYLINE)(lines))
VIEW(upLevel)
VIEW(OFFSET([.005,.005])(upLevel))
VIEW(SKEL_1(OFFSET([.005,.005])(upLevel)))

V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

thickWalls = sorted([7,1,12,5,22,  26,27,30,43,44,45])
thinWalls = set(range(len(EV))).difference(thickWalls)
thinHPCs = STRUCT(AA(POLYLINE)([[V[EV[e][0]],V[EV[e][1]]] for e in thinWalls]))
thickHPCs = STRUCT(AA(POLYLINE)([[V[EV[e][0]],V[EV[e][1]]] for e in thickWalls]))
thin = COLOR(YELLOW)(OFFSET([.0025,.0025])(thinHPCs))
thick = COLOR(CYAN)(OFFSET([.005,.005])(thickHPCs))
VIEW(STRUCT([ thin, thick ]))
VIEW(PROD([ STRUCT([thin,thick]), INTERVALS(3./24)(1) ]))

""" low floor of duplex  """

lines = lines2lines("up-level.lines")
V,EV = lines2lar(lines)
VV = AA(LIST)(range(len(V)))
larLowLevel1D = struct2lar(Struct([ t(1,0),s(-1,1),(V,EV) ]))
V,EV = larLowLevel1D
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.05))

thinWalls = sorted([45,64,35,39,63,  53,33,71,25,19,70,8,66,48,
7,58,68,  14,46,27,30,22,5,37,32,3,  56,59,54,15,21,36,6,62,4,16,61,0,55,57])  
thickWalls = set(range(len(EV))).difference(thinWalls)
thinHPCs = STRUCT(AA(POLYLINE)([[V[EV[e][0]],V[EV[e][1]]] for e in thinWalls]))
thickHPCs = STRUCT(AA(POLYLINE)([[V[EV[e][0]],V[EV[e][1]]] for e in thickWalls]))
thin = COLOR(YELLOW)(OFFSET([.0025,.0025])(thinHPCs))
thick = COLOR(CYAN)(OFFSET([.005,.005])(thickHPCs))
VIEW(STRUCT([ thin, thick ]))
VIEW(PROD([ STRUCT([thin,thick]), INTERVALS(3./24)(1) ]))

""" upper floor of duplex scaling  """

lines = lines2lines("floor-2.lines")
W,FW,EW,polygons = larFromLines(lines)
VIEW(SKEL_1(STRUCT(MKPOLS((W,EW)))))

def viewNumbers(numberSize):
	def viewNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return 	viewNumbers0

viewNumbers(.05)(W,EW,FW)

""" lower floor of duplex scaling  """

U,FU,EU = struct2lar(Struct([ t(1,0),s(-1,1),(W,FW,EW) ]))
viewNumbers(.05)(U,EU,FU)

