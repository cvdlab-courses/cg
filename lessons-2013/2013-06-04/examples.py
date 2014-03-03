from lar import *

FV = [[5,6,7,8],
[0,5,8],
[0,4,5],
[1,2,4,5],
[2,3,5,6],
[0,8,7], [3,6,7], [1,2,3], [0,1,4]
]

V = [[0,6],
[0,0],
[3,0],
[6,0],
[0,3],
[3,3],
[6,3],
[6,6],
[3,6]]

# out = MKPOL([V, [AA(lambda x: x+1)(f)  for f in FV], None ])

# VIEW(SKELETON(1)(out))

# csrFV = csrCreate(FV)

model = (V,FV)

V,EV = larFacets(model,dim=2)

# VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((V,EV))))

"""
models = ((V,EV),  ( [[0],[1]], [[0,1]] ))
V,F2V = larProduct(models)
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS(larProduct(models))))
"""

models = ((V,EV),  ( [[0.],[1.],[2.],[4.]], [[0],[1],[2],[3]] ))
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS(larProduct(models))))




