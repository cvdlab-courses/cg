
import sys
from larlib import *

sys.path.insert(0, '/Documents/DIDATTICA_2016/grafica/progetti/marsiglia/model/')
from model3 import *


def VIEWNumbers(numberSize):
	def VIEWNumbers0(V,EV,FV=[],CV=[]):
		submodel = STRUCT(MKPOLS((V,EV)))
		VV = AA(LIST)(range(len(V)))
		VIEW(larModelNumbering(1,1,1)(V,[VV,[],FV,CV],submodel,numberSize))
	return VIEWNumbers0

h = 3./24
H = INTERVALS(h)(1)

""" duplex apartment -- first draft """

lines = lines2lines("up-level.lines")
V,EV = lines2lar(lines,True)
upLevel = STRUCT(MKPOLS((V,EV)))
VIEW(upLevel)
upLevel = OFFSET([.0025,.0025])(upLevel)
VIEW(upLevel)
VIEW(SKEL_1(upLevel))
upWalls = PROD([ upLevel, H ])
VIEW(upWalls)
VIEW(SKEL_2(upWalls))


def convertIndices(vertDict,V,cells):
	numeral = OrderedDict([(key,k) for k,key in enumerate(vertDict.keys())])
	outcells = [[numeral[vcode(5)(V[v-1])] for v in cell] for cell in cells]
	return outcells

def plasm2lar(hpc):
	d = hpc.spacedim
	vertDict = defaultdict(list)
	if d==3:
		V3,CV3,_ = UKPOL(hpc)
		[vertDict[vcode(5)(vert)].append(vert) for vert in V3]
		len3 = len(vertDict)
		CV = convertIndices(vertDict,V3,CV3)
	if d>=2:
		V2,FV2,_ = UKPOL(SKEL_2(hpc))
		[vertDict[vcode(5)(vert)].append(vert) for vert in V2]
		len2 = len(vertDict)
		FV = convertIndices(vertDict,V2,FV2)
	if d>=1:
		V1,EV1,_ = UKPOL(SKEL_1(hpc))
		[vertDict[vcode(5)(vert)].append(vert) for vert in V1]
		len1 = len(vertDict)
		EV = convertIndices(vertDict,V1,EV1)
	assert len1==len2==len3
	V = AA(eval)(vertDict.keys())
	if d==3: return V,CV,FV,EV
	if d==2: return V,FV,EV
	if d==1: return V,EV

V,CV,FV,EV = plasm2lar(upWalls)
VIEW(STRUCT(MKPOLS((V,CV))))
VIEW(STRUCT(MKPOLS((V,FV))))
VIEW(STRUCT(MKPOLS((V,EV))))

BF = boundaryCells(CV,FV)
VIEW(STRUCT(MKPOLS((V,[FV[f] for f in BF]))))

struct2Marshal(Struct([V,FV,EV]))

