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







def Intervals(a):
	def Intervals0(n): return QUOTE(N(n)(a/n))
	return Intervals0

BaseHermite:(Intervals:1:20)

points = [[-0,0],[1,0],[1,1],[2,1],[3,1]]
VIEW(STRUCT([
			 POLYLINE(points),
			 MAP(BEZIER(S1)(points))(INTERVALS(1)(32))
			 ])
	 )

C0 = BEZIER(S1)([[0,0,0],[10,0,0]])
C1 = BEZIER(S1)([[0,2,0],[8,3,0],[9,2,0]])
C2 = BEZIER(S1)([[0,4,1],[7,5,-1],[8,5,1],[12,4,0]])
C3 = BEZIER(S1)([[0,6,0],[9,6,3],[10,6,-1]])

VIEW(MAP(BEZIER(S2)([C0,C1,C2,C3]))(PROD([INTERVALS(1)(10),INTERVALS(1)(10)])))





h1 = lambda u: 2*u**3 -3*u**2 + 1
h2 = lambda u: -2*u**3 + 3*u**2
h3 = lambda u: u**3 -2*u**2 + u
h4 = lambda u: u**3 - u**2


BaseHermite = [h1,h2,h3,h4]

def graph(function):
	def graph0(domain):
		u = lambda p: p[0]
		hpc = MAP([u, COMP([function,u])])(domain)
		return hpc
	return graph0
	
VIEW(graph(h1)(INTERVALS(1)(32)))

dom = INTERVALS(1)(32)
VIEW(STRUCT(CONS(AA(graph)(BaseHermite))(dom))+[SKEL_1(CUBOID([1,1]))])
	

def bezier(n):
	def bezier0(k):
		def bezier1(p):
			u = p[0]
			return CHOOSE([n,k])*u**k*(1-u)**(n-k)
		return bezier1
	return bezier0

bezier(2)(1)([0])

AA(bezier(2))([0,1,2])
CONS(AA(bezier(2))([0,1,2]))([0.5])

def test(n,u):
    return SUM(CONS(AA(bezier(n))(range(n+1)))([u]))

def bezierBasis(n):
	return AA(bezier(n))(range(n+1))

CONS(bezierBasis(3))([0.5])

