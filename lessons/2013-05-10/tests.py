from pyplasm import *
import scipy
from scipy import *

#---------------------------------------------------------
def VERTEXTRUDE((V,coords)):
    """
        Utility function to generate the output model vertices in a 
        multiple extrusion of a LAR model.
        V is a list of d-vertices (each given as a list of d coordinates).
        coords is a list of absolute translation parameters to be applied to 
        V in order to generate the output vertices.
        
        Return a new list of (d+1)-vertices.
    """
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def cumsum(iterable):
    # cumulative addition: list(cumsum(range(4))) => [0, 1, 3, 6]
    iterable = iter(iterable)
    s = iterable.next()
    yield s
    for c in iterable:
        s = s + c
        yield s

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])
#---------------------------------------------------------

domain=GRID([10]) #INTERVALS(1)(20)
points = [[1,-1],[-1,2],[1,4], [2,3],[0,0],[2.5,1],[3,-1], [1,-1],[-1,2],[1,4]];
points1 = [[1,-1],[-1,2],[1,4],[1,4], [2,3],[0,0],[2.5,1],[3,-1], [1,-1],[-1,2],[1,4]];
points2 = [[1,-1],[-1,2],[1,4],[1,4],[1,4], [2,3],[0,0],[2.5,1],[3,-1], [1,-1],[-1,2],[1,4]];
VIEW(STRUCT([
	POLYLINE(points),
	POLYMARKER(1)(points),
	COLOR(RED)(SPLINE(CUBICUBSPLINE(domain))(points)),
	COLOR(GREEN)(SPLINE(CUBICUBSPLINE(domain))(points1)),
	COLOR(YELLOW)(SPLINE(CUBICUBSPLINE(domain))(points2))
	]))


ControlPoints=[[0,0],[-1,2],[1,4],[2,3],[1,1],[1,2], [0,0],[-1,2],[1,4]]
VIEW(DISPLAYNUBSPLINE([3,[0,0,0,0, 1,2,3,4,5  ,6,6,6,6], ControlPoints]))



Su0 = BEZIER(S1)([[0,0,0],[10,0,0]])
Su1 = BEZIER(S1)([[0,10,0],[2.5,10,3],[5,10,-3],[7.5,10,3],[10,10,0]])
S0v = BEZIER(S2)([[0,0,0],[0,0,3],[0,10,3],[0,10,0]])
S1v = BEZIER(S2)([[10,0,0],[10,5,3],[10,10,0]])
VIEW(MAP(COONSPATCH([Su0,Su1,S0v,S1v]))(GRID([20,20])))



VIEW(MAP(BEZIER(S1)([[-0,0],[1,0],[1,1],[2,1],[3,1]]))(INTERVALS(1)(32)))
C0 = BEZIER(S1)([[0,0,0],[10,0,0]])
C1 = BEZIER(S1)([[0,2,0],[8,3,0],[9,2,0]])
C2 = BEZIER(S1)([[0,4,1],[7,5,-1],[8,5,1],[12,4,0]])
C3 = BEZIER(S1)([[0,6,0],[9,6,3],[10,6,-1]])
VIEW(MAP(BEZIER(S2)([C0,C1,C2,C3]))(GRID([20,20])))



Su0=BEZIER(S1)([[0,0,0],[10,0,0]])
Su1=BEZIER(S1)([[0,10,0],[2.5,10,3],[5,10,-3],[7.5,10,3],[10,10,0]])
Sv0=BEZIER(S2)([[0,0,0],[0,0,3],[0,10,3],[0,10,0]])
Sv1=BEZIER(S2)([[10,0,0],[10,5,3],[10,10,0]])
VIEW(MAP(COONSPATCH([Su0,Su1,Sv0,Sv1]))(GRID([20,20])))



alpha= lambda point: [point[0],point[0],       0 ]
beta = lambda point: [      -1,      +1,point[0] ]
domain= T([1,2])([-1,-1])(GRID([20,20]))
VIEW(MAP(RULEDSURFACE([alpha,beta]))(domain))



alpha=BEZIER(S1)([[0.1,0,0],[2,0,0],[0,0,4],[1,0,5]])
beta =BEZIER(S2)([[0,0,0],[3,-0.5,0],[3,3.5,0],[0,3,0]])
domain=GRID([20,20])
VIEW(STRUCT([MAP(alpha)(domain),MAP(beta )(domain),MAP(PROFILEPRODSURFACE([alpha,beta]))(domain)]))



profile=BEZIER(S1)([[0,0,0],[2,0,1],[3,0,4]]) # defined in xz!
domain=GRID([12,40])
VIEW(MAP(ROTATIONALSURFACE(profile))(S(2)(2*PI)(domain)))



alpha=BEZIER(S1)([[1,1,0],[-1,1,0],[1,-1,0],[-1,-1,0]])
Udomain=INTERVALS(1)(20)
Vdomain=INTERVALS(1)(6)
domain=GRID([20,20])
fn=CYLINDRICALSURFACE([alpha,[0,0,1]])
VIEW(MAP(fn)(domain))



domain=GRID([20,12])
beta=BEZIER(S1)([ [1,1,0],[-1,1,0],[1,-1,0],[-1,-1,0] ])
VIEW(MAP(CONICALSURFACE([[0,0,1],beta]))(domain))



domain1D=INTERVALS(1)(20)
VIEW(STRUCT(
	[MAP(CUBICHERMITE(S1)([[1,0],[1,1],[ -1, 1],[ 1,0]]))(domain),
    MAP(CUBICHERMITE(S1)([[1,0],[1,1],[ -2, 2],[ 2,0]]))(domain1D),
    MAP(CUBICHERMITE(S1)([[1,0],[1,1],[ -4, 4],[ 4,0]]))(domain1D),
    MAP(CUBICHERMITE(S1)([[1,0],[1,1],[-10,10],[10,0]]))(domain1D)]))



c1=CUBICHERMITE(S1)([[1  ,0,0],[0  ,1,0],[0,3,0],[-3,0,0]])
c2=CUBICHERMITE(S1)([[0.5,0,0],[0,0.5,0],[0,1,0],[-1,0,0]])
sur3=CUBICHERMITE(S2)([c1,c2,[1,1,1],[-1,-1,-1]])
domain2D=GRID([20,12])
VIEW(MAP(sur3)(domain))




domain=INTERVALS(1)(20)
points = [[-3,6],[-4,2],[-3,-1],[-1,1],[1.5,1.5],[3,4],[5,5],[7,2],[6,-2],[2,-3]]
VIEW(SPLINE(CUBICCARDINAL(domain))(points))
VIEW(SPLINE(CUBICUBSPLINE(domain))(points))



controlpoints=[[[0,0,0],[2,-4,2]],[[0,3,1],[4,0,0]]]
domain=GRID([20,20])
mapping=BILINEARSURFACE(controlpoints)
VIEW(MAP(mapping)(domain))



controlpoints=[[[0,0,0],[2,0,1],[3,1,1]],[[1,3,-1],[3,2,0],[4,2,0]],[[0,9,0],[2,5,1],[3,3,2]]]
domain=GRID([20,20])
mapping=BIQUADRATICSURFACE(controlpoints)
VIEW(MAP(mapping)(domain))



controlpoints=[[[0,0,0 ],[2,0,1],[3,1,1],[4,1,1]],
				[[1,3,-1],[3,2,0],[4,2,0],[4,2,0]],
				[[0,4,0 ],[2,4,1],[3,3,2],[5,3,2]],
				[[0,6,0 ],[2,5,1],[3,4,1],[4,4,0]]]
domain=GRID([20,20])
mapping=HERMITESURFACE(controlpoints)
VIEW(MAP(mapping)(domain))



controlpoints=[
[[ 0,0,0],[0 ,3  ,4],[0,6,3],[0,10,0]],
[[ 3,0,2],[2 ,2.5,5],[3,6,5],[4,8,2]],
[[ 6,0,2],[8 ,3 , 5],[7,6,4.5],[6,10,2.5]],
[[10,0,0],[11,3  ,4],[11,6,3],[10,9,0]]]
domain=GRID([20,20])
mapping=BEZIERSURFACE(controlpoints)
hpc = MAP(mapping)(domain)
VIEW(hpc)



domain3D=GRID([20,20,4])
degrees = [2,2,2]
Xtensor =  [[[0,1,2],[-1,0,1],[0,1,2]],[[0,1,2],[-1,0,1],[0,1,2]],[[0,1,2],[-1,0,1],[0,1,2]]]
Ytensor =  [[[0,0,0.8],[1,1,1],[2,3,2]],[[0,0,0.8],[1,1,1],[2,3,2]],[[0,0,0.8],[1,1,1],[2,3,2]]]
Ztensor =  [[[0,0,0],[0,0,0],[0,0,0]],[[1,1,1],[1,1,1],[1,1,1]],[[2,2,1],[2,2,1],[2,2,1]]] 
mapping = BEZIERMANIFOLD(degrees)([Xtensor,Ytensor,Ztensor])
VIEW(MAP(mapping)(domain3D))



verts = [[0,0,0],[3,0,0],[3,2,0],[0,2,0],[0,0,1.5],[3,0,1.5],[3,2,1.5],[0,2,1.5],[0,1,2.2],[3,1,2.2]]
cells = [[1,2],[2,3],[3,4],[4,1],[5,6],[6,7],[7,8],[8,5],[1,5],[2,6],[3,7],[4,8],[5,9],[8,9],[6,10],[7,10], [9,10]]
pols = [[1]]
House = MKPOL([verts,cells,pols])
VIEW(STRUCT([OFFSET([0.1,0.2,0.1])(House), T(1)(1.2*SIZE(1)(House))(House)]))


VIEW(OFFSET([0.1,0.2,0.1])(hpc))

dom3D = INSR(PROD)([INTERVALS(1)(5),INTERVALS(1)(5),INTERVALS(1)(5)])
VIEW(OFFSET([0.01,0.01,0.03])(SKELETON(1)(dom3D)))


Su0 = COMP([BEZIERCURVE([[0,0,0],[10,0,0]]),CONS([S1])])
Su1 = COMP([BEZIERCURVE([[0,10,0],[2.5,10,3],[5,10,-3],[7.5,10,3],[10,10,0]]),CONS([S1]) ])
S0v = COMP([BEZIERCURVE([[0,0,0],[0,0,3],[0,10,3],[0,10,0]]) , CONS([S2]) ]) 
S1v = COMP([BEZIERCURVE([[10,0,0],[10,5,3],[10,10,0]]) ,CONS([S2])   ])
surface=COONSPATCH([Su0,Su1,S0v,S1v])

VIEW(MAP(  surface ) (GRID([20,20])))
solidMapping = THINSOLID(surface)

Domain3D = PROD([PROD([INTERVALS(1)(10),INTERVALS(1)(10)]),INTERVALS(0.5)(1)])
VIEW(MAP(solidMapping)(Domain3D))




VIEW(ELLIPSE([1,2])(8))




vertices = [[0,0],[1.5,0],[-1,2],[2,2],[2,0]]
VIEW(STRUCT([
	POLYLINE(vertices),
	BEZIERSTRIPE([vertices,0.25,66])
	]))
	
	
VIEW(STRUCT([
	POLYLINE(vertices),
	PROD([ BEZIERSTRIPE([vertices,0.25,66]), QUOTE([0.9]) ])
	]))



ControlPoints=[[0,0],[-1,2],[1,4],[2,3],[1,1],[1,2],[2.5,1], [2.5,3], [4,4],[5,0]]
VIEW(DISPLAYNUBSPLINE([3,[0,0,0,0, 1,2,3,4,5, 6    ,7,7,7,7], ControlPoints]))



knots = [0,0,0,1,1,2,2,3,3,4,4,4]
_p=math.sqrt(2)/2.0
controlpoints = [[-1,0,1], [-_p,_p,_p], [0,1,1], [_p,_p,_p],[1,0,1], [_p,-_p,_p], [0,-1,1], [-_p,-_p,_p], [-1,0,1]]
VIEW(DISPLAYNURBSPLINE([2, knots, controlpoints]))




