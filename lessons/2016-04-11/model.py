from larlib import *

""" Input pilotis (struttura-base) """

filename = "struttura-base.svg"
lines = svg2lines(filename)
VIEW(STRUCT(AA(POLYLINE)(lines)))

""" Calcolo e visualizzazione celle complesso pilotis 2D """

V,FV,EV,polygons = larFromLines(lines)
VIEW(EXPLODE(1.2,1.2,1)(MKPOLS((V,EV)) + AA(MK)(V)))
VIEW(EXPLODE(1.2,1.2,1)(MKTRIANGLES((V,FV,EV)) + AA(MK)(V)))
VIEW(STRUCT(MKTRIANGLES((V,FV,EV)) + AA(MK)(V)))

colors = [CYAN,MAGENTA,WHITE,RED,YELLOW,GREEN,GRAY,ORANGE, BLACK,BLUE,PURPLE,BROWN]
VIEW(STRUCT([COLOR(colors[k%12])(cell) for k,cell in enumerate( MKTRIANGLES((V,FV,EV))) ]))

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))

""" Scaling to true measures (in meters) """

EV[27] == [29, 7]
V[29], V[7] == ([0.0, 1.0], [1.0, 1.0])
"""
16 x 4.8x2 = 16 x 9.6 = 153.6
24 - 2 x 1.2 = 21.6
"""
delta_x_basement = 21.6
# W = SCALARMATPROD([delta_x_basement,V])
W = ((mat(V) - V[12]) * 21.6).tolist()

""" Definition of semantics of some 2-subcomplexes """

pillar = (W,[FV[k] for k in [0,1,3,4,5]])
slab = (W,[FV[k] for k in [2]])
VIEW(EXPLODE(1.2,1.2,1)(MKPOLS(pillar)+MKPOLS(slab)))

""" Generation of 3D pilotis """

pillarPattern = 17*[1.2,-8.4]
VIEW(STRUCT(MKPOLS(larQuote1D(pillarPattern))))
pillars = larModelProduct([pillar,larQuote1D(pillarPattern)])
VIEW(STRUCT(MKPOLS(pillars)))

slabPattern = 16*[1.2,8.4]+[1.2]
slabs = larModelProduct([slab,larQuote1D(slabPattern)])
VIEW(STRUCT(MKPOLS(slabs)))

VIEW(STRUCT(MKPOLS(pillars)+MKPOLS(slabs)))

""" Telaio monopiano (spazio normalizzato) """

filename = 'travePilastri.svg'
linesTravePilastri = svg2lines(filename)
VIEW(STRUCT(AA(POLYLINE)(linesTravePilastri)))
P,FP,EP,polygons = larFromLines(linesTravePilastri)
PP = AA(LIST)(range(len(P)))
submodel = STRUCT(MKPOLS((P,EP)))
VIEW(larModelNumbering(1,1,1)(P,[PP,EP,FP],submodel,0.075))

pilastri = (P,[FP[k] for k in [0,12,13,14,15,16]])
traveLongitudinale = (P,[FP[k] for k in [6,7,8,9,10,11]])
traviTrasversali = (P,[FP[k] for k in [1,2,3,4,5]])
VIEW(STRUCT(MKPOLS(pilastri)+MKPOLS(traveLongitudinale)+MKPOLS(traviTrasversali)))
VIEW(EXPLODE(1.2,1.2,1)(MKPOLS(pilastri)+MKPOLS(traveLongitudinale)+MKPOLS(traviTrasversali)))

""" Grid per telaio multipiano """

filename = 'grid.svg'
linesGrid = svg2lines(filename)
VIEW(STRUCT(AA(POLYLINE)(linesGrid)))
P,FP,EP,polygons = larFromLines(linesGrid)
PP = AA(LIST)(range(len(P)))
submodel = STRUCT(MKPOLS((P,EP)))
VIEW(larModelNumbering(1,1,1)(P,[PP,EP,FP],submodel,0.025))

""" Trasformazione a coordinate vere (coordinate mondo) """

Delta_x_telaio = P[130][0]-P[63][0]
scale_telaio = delta_x_basement/Delta_x_telaio
X = ((mat(P)-P[63]) * scale_telaio + W[29]).tolist()
VIEW(SKEL_1(STRUCT(MKPOLS((X,FP))+MKPOLS(pillar)+MKPOLS(slab))))

""" eliminazione 2-celle vuote dal telaio """

campate = sorted([127,131,129,128,130,107,108,110,111,109,
102,106,105,103,104,
114,115,117,124,116,119,125,113,118,112,120,123,121,126,122])

campate == range(102,132)
len(FP) == 132
telaio = (X,[FP[k] for k in range(102)])
VIEW(STRUCT(MKPOLS(telaio)+MKPOLS(pillar)+MKPOLS(slab)))
VIEW(EXPLODE(1.2,1.2,1)(MKPOLS(telaio)+MKPOLS(pillar)+MKPOLS(slab)))



"""  Costruzione telaio 3D """

VIEW(STRUCT(MKPOLS(telaio)+MKPOLS(pillars)+MKPOLS(slabs)))

concreteFramePattern = 16*[-0.4,0.4,-0.4, -8.4]+[-0.4,0.4,-0.4]
concreteFrame = larModelProduct([telaio,larQuote1D(concreteFramePattern)])
VIEW(STRUCT(MKPOLS(concreteFrame)+MKPOLS(pillars)+MKPOLS(slabs)))

crossBeams = sorted([30,22,12,6,20,8,15,7,32,16,24,31,9,18,28,33,17,25,19,14,35,13,21,11,26,23,34,29,27,10,0,4,2,1,5,3])

range(36) == sorted(crossBeams)
crossBeam = (X,[FP[k] for k in range(36)])
VIEW(STRUCT(MKPOLS(crossBeam)))

concreteCrossBeamsPattern = [-0.4]+16*[0.8,8.8]+[0.4]
concreteCrossBeams = larModelProduct([crossBeam,larQuote1D(concreteCrossBeamsPattern)])
VIEW(STRUCT(MKPOLS(concreteFrame)+MKPOLS(pillars)+MKPOLS(slabs)+MKPOLS(concreteCrossBeams)))

"""  Rotazione nel riferimento ingegneristico """

frame = struct2lar(Struct([pillars,concreteFrame,slabs,concreteCrossBeams]))
Q,CQ = frame
frame = AA(CONS([S3,S1,S2]))(Q),CQ
VIEW(STRUCT(MKPOLS(frame) ))

""" Input of building entrance """

filename = "entree.lines"
lines = lines2lines(filename)
VIEW(STRUCT(AA(POLYLINE)(lines)))

Y,FY,EY,polygons = larFromLines(lines)
VIEW(STRUCT(MKPOLS((Y,EY))))
VIEW(STRUCT(MKTRIANGLES((Y,FY,EY))))

YY = AA(LIST)(range(len(Y)))
submodel = STRUCT(MKPOLS((Y,EY)))
VIEW(larModelNumbering(1,1,1)(Y,[YY,EY,FY],submodel,0.25))

""" entrance scaling and positioning """

EY[29] == [32, 14]
scaling = 9./(Y[32][0] - Y[14][0])*1.5
Z = ((mat(Y)-Y[14])*scaling + [8*9.6+.8,-3.63]).tolist()
#Z = (Z+[9.6+.4]).tolist()
entree = (Z,FY,EY)
VIEW(STRUCT(MKPOLS(frame)+MKTRIANGLES(entree)))

entranceSurface = entree[0],entree[2]
stairCasePattern = 8*[6.0]
stairCase = larModelProduct([entranceSurface,larQuote1D(stairCasePattern)])
VIEW(STRUCT(MKPOLS(frame)+MKPOLS(stairCase)))

