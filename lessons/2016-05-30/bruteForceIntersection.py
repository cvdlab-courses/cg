lines = [
 [[0.0, 0.0], [-0.1, 0.0]],
 [[0.0, 0.0], [-1.221245327087672e-16, -1.1]],
 [[-1.1, 2.220446049250313e-16], [-1.1000000000000003, -1.0999999999999999]],
 [[-1.221245327087672e-16, -1.1], [-0.10000000000000013, -1.1]],
 [[-1.1000000000000003, -1.0999999999999999],
  [-1.1000000000000003, -0.9999999999999999]],
 [[-1.1000000000000003, -1.0999999999999999], [-1.221245327087672e-16, -1.1]],
 [[-1.1000000000000003, -0.9999999999999999], [-1.1102230246251564e-16, -1.0]],
 [[0.0, 0.0], [-1.1, 2.220446049250313e-16]],
 [[-1.221245327087672e-16, -1.1], [-1.1102230246251564e-16, -1.0]],
 [[-0.10000000000000013, -1.1], [-0.1, 0.0]]]

def bruteForceIntersect(lines):
	n = len(lines)
	#transform data
	lines = [[eval(vcode(4)(p)) for p in line] for line in lines]
	#end transform
	verts = list(set([tuple(v) for line in lines for v in line]))
    vertdict = OrderedDict([(key,k) for k,key in enumerate(verts)])
	EV = [[vertdict[tuple(p)] for p in line] for line in lines]
    pairs = [(h,k) for h in range(n) for k in range(h+1,n)]
    linepairs = [[lines[h],lines[k]] for h,k in pairs]
    # prepare data for line pairs
    linedata = [[ax,ay,bx,by,cx,cy,dx,dy] 
        for [[(ax,ay),(bx,by)],[(cx,cy),(dx,dy)]] in linepairs]
    # assemble intersection determinants
    determinants = [ det(mat([[ax-bx,dx-cx], [ay-by,dy-cy]])) 
        for [ax,ay,bx,by,cx,cy,dx,dy] in linedata]
    # parameter pairs by Cramer's rule (for oriented edges of f face)
    alpha = [det(mat([[dx-bx,dx-cx],[dy-by,dy-cy]]))/D  if abs(D)>.00001 else 0 
        for D,(ax,ay,bx,by,cx,cy,dx,dy) in zip(determinants,linedata)]
    beta = [det(mat([[ax-bx,dx-bx],[ay-by,dy-by]]))/D  if abs(D)>.00001 else 0 
        for D,(ax,ay,bx,by,cx,cy,dx,dy) in zip(determinants,linedata)]
    # intersection points
    vdata,edata = defaultdict(list),defaultdict(list)
    newverts = [ tuple(AA(COMP([tuple,eval,vcode(4)]))([ 
        (a*mat(p1)+(1-a)*mat(p2)).tolist()[0], 
        [a,b,h,k] ]))
        for (a,b,(h,k)),[[p1,p2],[q1,q2]] in zip(zip(alpha,beta,pairs),linepairs) 
        if 0<=a<=1 and 0<=b<=1 ]
    for vert,datum in newverts:
       vdata[vert] += [datum]
    for k,(key,datum) in enumerate(vdata.items()):
        print k,(key,datum)
        for a,b,edge1,edge2 in datum:
            edata[int(edge1)] += [a]
            edata[int(edge2)] += [b]
    edgeParameters = [sorted(set(edge)) for k,edge in edata.items()]
    points = [[(a*mat(verts[p])+(1-a)*mat(verts[q])).tolist()[0] 
            for a in params] for params,(p,q) in zip(edgeParameters,EV)]
    m = len(vertdict)
    for point in CAT(points):
        vertex = tuple(eval(vcode(4)(point)))
        if not vertex in vertdict:
            vertdict[vertex] = m
            m += 1
    edgeVerts = [[vertdict[tuple(eval(vcode(4)(point)))] for point in edge] 
        for edge in points]
    V = AA(list)(vertdict.keys())
    edges = [[[v,part[k+1]] for k,v in enumerate(part[:-1])] for part in edgeVerts]
    EV = sorted(set(AA(tuple)(AA(sorted)(CAT(edges)))))
    return V,EV
@}
