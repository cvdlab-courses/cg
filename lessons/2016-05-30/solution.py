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
	verts = list(set([tuple(eval(vcode(4)(v)))
					  for line in lines for v in line]))
	vertdict = OrderedDict([(key,k) for k,key in enumerate(verts)])
	EV = [[vertdict[tuple(eval(vcode(4)(p)))]
		   for p in line] for line in lines]
	
	
	linedata =[[[a,b,c,d] for k,(c,d) in enumerate(lines) if k!=h ]
		for h,(a,b) in enumerate(lines)]
	determinants = [[det(mat([[ax-bx,dx-cx], [ay-by,dy-cy]]))
	  for (ax,ay),(bx,by),(cx,cy),(dx,dy) in line]
	  for line in linedata]
	alphaPerLine = [[det(mat([[ax-bx,dx-bx],[ay-by,dy-by]]))/D
	  if abs(D)>.00001 else -1
	  for D,((ax,ay),(bx,by),(cx,cy),(dx,dy)) in zip(dets,thelines)]
	  for dets,thelines in zip(determinants,linedata)]
	  
	  
	  AA(TRANS)(TRANS([alphaPerLine,linedata]))
	  
	  
	parameters = [[[a,data] for a,data in zip(alphas, line) if 0<=a<=1]
	  for alphas,line in zip(alphaPerLine,lines)]
	  
	pointsPerLine = [[ tuple(eval(vcode(4)(
	  (a*mat(p2)+(1-a)*mat(p1)).tolist()[0]))) for a in pars]
	  for pars,(p1,p2) in zip(parameters,lines)]
	newlines = CAT([[[p,points[k+1]] for k,p in enumerate(points[:-1])]
	  for points in pointsPerLine])
	  
	  
	  
	verts =
	vertdict = OrderedDict([(key,k) for k,key in enumerate(verts)])
	EV = [[vertdict[tuple(eval(vcode(4)(p)))] for p in line] for line in newlines]



return V,EV

V,EV = bruteForceIntersect(lines)

submodel = STRUCT(MKPOLS((V,EV)))
VV = AA(LIST)(range(len(V)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV],submodel,0.5))


