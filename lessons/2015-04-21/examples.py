from pyplasm import *

def bezierBasis(n):
    def bezierBasis0(u):
        basis = []
        for k in range(n+1):
            bernstein = CHOOSE([n,k])*((1-u)**(n-k))*(u**k)
            basis += [bernstein]
        return basis
    return bezierBasis0

def bezier(points):
    def bezier0(p):
        u = p[0]
        n = len(points)-1
        basis = bezierBasis(n)(u)
        handles = TRANS(points)
        out = AA(INNERPROD)(DISTL([basis,handles]))
        return out
    return bezier0


points1 = [[0,0],[1,1]]
points2 = [[0,0],[1,0],[1,1]]
points3 = [[0,0],[1,0],[0,1],[1,1]]
points4 = [[0,0],[1,0],[1,1],[0,1],[0,0]]

bezier(points1)([0.5])

VIEW(MAP(bezier(points2))(INTERVALS(1)(32)))

VIEW(STRUCT(
            [POLYLINE(points3),
             MAP(bezier(points3))(INTERVALS(1)(32))]
            ))

VIEW(STRUCT(
            [POLYLINE(points4),
             MAP(bezier(points4))(INTERVALS(1)(132))]
            ))

