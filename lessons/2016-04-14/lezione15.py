from larlib import *

""" scala lineare 2.5-dimensionale """

lines = lines2lines("scala.lines")
V,FV,EV,polygons = larFromLines(lines)
FV = sorted(FV,key=lambda cell: CCOMB([V[k] for k in cell])[0])
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((V,EV))))
VIEW(EXPLODE(1.2,1.2,1.2)(MKFACES((V,FV,EV))))

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))
