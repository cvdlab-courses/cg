import sys
from larlib import *

sys.path.insert(0, '/Documents/DIDATTICA_2016/grafica/progetti/marsiglia/model/')
from model import *

def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0

h = 3./24
H = INTERVALS(h)(1)

""" duplex apartment -- first draft """

lines = lines2lines(project_path + "up-level.lines")
V,EV = lines2lar(lines,True)
upLevel = STRUCT(MKPOLS((V,EV)))
#VIEW(upLevel)
upLevel = OFFSET([.0025,.0025])(upLevel)
#VIEW(upLevel)
#VIEW(SKEL_1(upLevel))
upWalls = PROD([ upLevel, H ])
#VIEW(upWalls)

lines = lines2lines(project_path + "mid-level.lines")
V,EV = lines2lar(lines,True)
midLevel = STRUCT(MKPOLS((V,EV)))
#VIEW(midLevel)
midLevel = OFFSET([.0025,.0025])(midLevel)
#VIEW(midLevel)
#VIEW(SKEL_1(midLevel))
midWalls = PROD([ midLevel, H ])
#VIEW(midWalls)

lines = lines2lines(project_path + "up-level.lines")
V,EV = lines2lar(lines,True)
VV = AA(LIST)(range(len(V)))
V,EV = struct2lar(Struct([ t(1,0),s(-1,1),(V,EV) ]))
lowLevel = STRUCT(AA(POLYLINE)([[V[u],V[v]] for u,v in EV]))
#VIEW(lowLevel)
lowLevel = OFFSET([.0025,.0025])(lowLevel)
#VIEW(SKEL_1(lowLevel))
lowWalls = PROD([ lowLevel, H ])
#VIEW(lowWalls)


""" upper floor of duplex scaling  """

lines = lines2lines(project_path + "floor-2a.lines")

W,FW,EW,polygons = larFromLines(lines,True)
#VIEWNumbers(.05)(W,EW,FW)
floor2 = [FW[k]  for k in [0,1,4,6]]
floor2 = MKTRIANGLES((W,floor2,[edge for edge in EW if set(edge).intersection(CAT(floor2))==set(edge)]))
upFloor = PROD([ PROJECT(1)(STRUCT(floor2)), INTERVALS(.3/24)(1) ])
VIEW(upFloor)

""" lower floor of duplex scaling  """

U,FU,EU = struct2lar(Struct([ t(1,0),s(-1,1),(W,FW,EW) ]))
VIEWNumbers(.05)(U,EU,FU)
floor1 = [FU[k]  for k in [6,4,0,2]]
floor1 = MKTRIANGLES((U,floor1,[edge for edge in EU if set(edge).intersection(CAT(floor1))==set(edge)]))
lowFloor = PROD([ PROJECT(1)(STRUCT(floor1)), INTERVALS(.3/24)(1) ])
VIEW(lowFloor)


""" Assembly of two duplex apartments  """

twoDuplex = TREE(TOP)([lowWalls,midWalls,upWalls])
#VIEW(twoDuplex)

interior = STRUCT(MKPOLS((W,[FW[k]  for k in [0,1]])))
c = MED([1,2])(interior)
xsize = eval(vcode(4)([SIZE(1)(interior)]))[0]
assert xsize == 0.8593

p = 1./xsize
scale = S([1,2,3])([p,p])
upFloor = STRUCT([T([1,2])(c), scale, T([1,2])([-c[0],-c[1]]), upFloor])
lowFloor = STRUCT([T([1,2])(c), scale, T([1,2])([-c[0],-c[1]]), lowFloor])

base = BOX([1,2,3])(STRUCT([lowFloor,upFloor]))
ymin = MIN(2)(base)

duplex_A = STRUCT([T(2)(-ymin),base,
twoDuplex,T(3)(h),lowFloor,T(3)(h),upFloor,T(3)(h*1),base])

VIEW(duplex_A)
doubleDuplex = STRUCT([S(2)(-1),duplex_A,S(2)(-1),duplex_A])
ymax = MIN(2)(doubleDuplex)
doubleDuplex = MAP(CONS([S2,S1,S3]))(STRUCT([T(2)(-ymax),doubleDuplex]))
VIEW(doubleDuplex)

""" Single pair of duplex apartments  """

singleDuplex = MAP(CONS([S2,S1,S3]))(duplex_A)

""" Smaller apartments for the building head """

# TODO: duplex_B

""" Exterior lateral frame """

q=h*18.17
xlines = larQuote1D([-0.4]+14*[4.8,4.8]+[0.4])
ylines = larQuote1D([-6.3]+[2*q,1*q, 2*q,1*q, 1.2*q,1.2*q, 2*q,1*q, 2*q,1*q, 2*q,1*q])
xylines = larModelProduct([xlines,ylines])
xyframe = OFFSET([.15*q,.15*q])(SKEL_1(STRUCT(MKPOLS(xylines))))
xyzframe = MAP(CONS([S1,S3,S2]))(PROD([xyframe,QUOTE([1.6])]))
VIEW(xyzframe)

""" Building module  """

firstFlat = 14*[doubleDuplex,T(1)(0.385)] + [singleDuplex]	
h = 3./24

""" Whole building assembly """

building = STRUCT( [COLOR(YELLOW)(STRUCT(MKPOLS(frame))), 
	T(2)(-3.3*1.5)(xyzframe),T(2)(17.8)(xyzframe),
	T([1,2,3])([0.6,-3.3,6.3]), S([1,2,3])([24.91,21.,18.17])] + 
	firstFlat + [T(3)(3*h), T(1)(14*-.385)] + 
	firstFlat + [T(3)(5.35*h), T(1)(14*-.385)] + 
	firstFlat + [T(3)(3*h), T(1)(14*-.385)] + 
	firstFlat + [T(3)(3*h), T(1)(14*-.385)] + 
	firstFlat 
	)
	
VIEW(building)
