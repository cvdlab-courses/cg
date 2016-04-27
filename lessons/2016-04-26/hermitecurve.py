def h1(u): return 2*u**3 -3*u**2 + 1
def h2(u): return -2*u**3 + 3*u**2
def h3(u): return u**3 -2*u**2 + u
def h4(u): return u**3 - u**2

u=0.5
p1 = [0,0]
p2 = [3,0]
t1 = [1,1]
t2 = [2,2]
[[h1(u),h2(u),h3(u),h4(u)],[p1,p2,t1,t2]]
[[h1(u),h2(u),h3(u),h4(u)],TRANS([p1,p2,t1,t2])]
DISTL([[h1(u),h2(u),h3(u),h4(u)],TRANS([p1,p2,t1,t2])])
AA(INNERPROD)(DISTL([[h1(u),h2(u),h3(u),h4(u)],TRANS([p1,p2,t1,t2])]))
hermite(p1,p2,t1,t2)
hermite(p1,p2,t1,t2)([0.5])
hermite(p1,p2,t1,t2)([0.75])
hermite(p1,p2,t1,t2)([0.])
hermite(p1,p2,t1,t2)([1.])
MAP(hermite(p1,p2,t1,t2))(INTERVALS(1)(32))
VIEW(MAP(hermite(p1,p2,t1,t2))(INTERVALS(1)(32)))

def hermite(p1,p2,t1,t2):
    h1 = lambda u: 2*u**3 -3*u**2 + 1
    h2 = lambda u: -2*u**3 + 3*u**2
    h3 = lambda u: u**3 -2*u**2 + u
    h4 = lambda u: u**3 - u**2
    def hermite0(p):
        u = p[0]
        basis = [h1(u),h2(u),h3(u),h4(u)]
        handles = TRANS([p1,p2,t1,t2])
        out = AA(INNERPROD)(DISTL([basis,handles]))
        return out
    return hermite0
    
hpc = MAP(hermite([0,0,1],[3,0,2],[10,10,-1],[2,2,0]))(INTERVALS(1)(32))

VIEW(hpc)


bezierBasis(n):

	return basis

def bezier(points):
    def hermite0(p):
        u = p[0]
        basis = bezierBasis(n)
        handles = TRANS(points)
        out = AA(INNERPROD)(DISTL([basis,handles]))
        return out
    return hermite0






