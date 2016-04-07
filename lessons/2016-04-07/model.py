from larlib import *

filename = "struttura-base.svg"
lines = svg2lines(filename)
VIEW(STRUCT(AA(POLYLINE)(lines)))
    
V,FV,EV,polygons = larFromLines(lines)

VIEW(EXPLODE(1.2,1.2,1)(MKPOLS((V,EV)) + AA(MK)(V)))
VIEW(EXPLODE(1.2,1.2,1)(MKTRIANGLES((V,FV,EV)) + AA(MK)(V)))
VIEW(STRUCT(MKTRIANGLES((V,FV,EV)) + AA(MK)(V)))

colors = [CYAN,MAGENTA,WHITE,RED,YELLOW,GREEN,GRAY,ORANGE,BLACK,BLUE,PURPLE,BROWN]
[COLOR(colors[k%12])(cell) for k,cell in enumerate(MKTRIANGLES((V,FV,EV))) ]
VIEW(STRUCT([COLOR(colors[k%12])(cell) for k,cell in enumerate(MKTRIANGLES((V,FV,EV))) ]))

VV = AA(LIST)(range(len(V)))
submodel = STRUCT(MKPOLS((V,EV)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV],submodel,0.1))


"""
16 x 4.8x2 = 16 x 9.6 = 153.6
24 - 2 x 1.2 = 21.6
"""

W = SCALARMATPROD([21.6,V])
W = ((mat(V) - V[12]) * 21.6).tolist()

pillar = (W,[FV[k] for k in [0,1,3,4,5]])
slab = (W,[FV[k] for k in [2]])
VIEW(STRUCT(MKPOLS(pillar)))

pillarPattern = 17*[1.2,-8.4]
VIEW(STRUCT(MKPOLS(larQuote1D(pillarPattern))))
pillars = larModelProduct([pillar,larQuote1D(pillarPattern)])
VIEW(STRUCT(MKPOLS(pillars)))

slabPattern = 17*[1.2,8.4]
slabs = larModelProduct([slab,larQuote1D(slabPattern)])
VIEW(STRUCT(MKPOLS(slabs)))

VIEW(STRUCT(MKPOLS(pillars)+MKPOLS(slabs)))





