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


def circle(r=1):
    x = lambda p: r*COS(p[0])
    y = lambda p: r*SIN(p[0])
    return CONS([x,y])


def circle(r=1):
    x = lambda p: r*COS(p[0])
    y = lambda p: r*SIN(p[0])
    z = lambda p: PROD([x(p),y(p)])
    return [x,y,z]


def circle(r=1):
    def circle0(p):
        u = p[0]
        x = r*COS(u)
        y = r*SIN(u)
        z = x*y
        return [x,y,z]
    return circle0



def dom(interval=1,dmin=0,dmax=1,steps=32):
    interval = interval*(dmax - dmin)
    return T(1)(dmin)(INTERVALS(interval)(steps))


VIEW(MAP(circle(1))(dom(1)))
VIEW(MAP(circle(1))(dom(2*PI)))
VIEW(MAP(circle(1))(dom(-PI,PI)))
VIEW(MAP(circle(1))(dom(-PI/2,3*PI/2)))



def beta(p):
    """ cross-section curve """
    u = p[0]
    x = COS(u)
    y = SIN(u)
    z = 0
    return [x,y,0]

VIEW(MAP(beta)(dom(2*PI)))

def alpha(p):
    """ profile curve """
    c = bezier([[0,0,0],[4,0,0],[6,0,2],[0,0,4],[2,0,5]])
    x = c(p)[0]
    y = c(p)[1]
    z = c(p)[2]
    return [x,y,z]


VIEW(MAP(alpha)(dom(1)))


def profileProduct(alpha,beta):
    def profileProduct0(p):
        u,v = p
        x = beta([u])[0] * alpha([v])[0]
        y = beta([u])[1] * alpha([v])[0]
        z = alpha([v])[2]
        return [x,y,z]
    return profileProduct0

domain = PROD([dom(interval=2*PI,steps=32),dom(steps=12)])

VIEW(GMAP(profileProduct(alpha,beta))(domain))







