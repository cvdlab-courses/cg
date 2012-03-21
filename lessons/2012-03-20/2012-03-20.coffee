###
#---------------------------------------------------
Computational Graphics 2012
Lab Examples of MAP primitive
REMARK:  in order to execute a single example,
move the two comment marks (three # chars) at the begin and end of its text slot.
#---------------------------------------------------
##
graph = (f) -> ([a,b]) ->
	PRINT "[a,b] =", [a,b]
	domain = INTERVALS(b-a)(30)
	PRINT "domain =", domain
	domain = T([0])([a]) domain
	PRINT "domain =", domain
	MAP([ID, f]) domain
	
object = graph(Math.sin)([-Math.PI, Math.PI])
PRINT "object =", object

model = viewer.draw object
##
#---------------------------------------------------
##
domain = INTERVALS(2*Math.PI)(30)
object = (MAP [Math.cos, Math.sin]) domain
##
#---------------------------------------------------
##
circle = (r) -> (c) -> (n) ->
	domain = INTERVALS(2*Math.PI)(n)
	x = (u) -> r * Math.cos u
	y = (u) -> r * Math.sin u
	object = T([0,1])(c) MAP([x, y])(domain)
	
object = circle(0.5)([0.5, 0.5]) 32
PRINT "object =", object

model = viewer.draw circle(0.5)([0.5, 0.5])(32)
##
#---------------------------------------------------
##
helix = (r=1, h=1, turns=6, n=180) ->
	domain = INTERVALS( turns*2*Math.PI )(n)
	x = (u) -> r * Math.cos u
	y = (u) -> r * Math.sin u
	z = (u) -> u * h/(turns*2*Math.PI)
	object = MAP([x, y, z])(domain)
	
object = helix()
PRINT "object =", object

model = viewer.draw object
##
#---------------------------------------------------
###
DISK = (radius=1,n=32,m=1) ->
	domain = SIMPLEXGRID [REPEAT(n)(2*Math.PI/n), REPEAT(m)(radius/m)]
	fx = ([u,v]) -> v*Math.sin(-u)
	fy = ([u,v]) -> v*Math.cos(-u)
	MAP( [fx, fy] )(domain)
	
#model = viewer.draw DISK(1,32,3)
#model = viewer.draw R([0,2])(Math.PI) EMBED(1) DISK(1,32)
#model = viewer.draw SKELETON(1) DISK(1,32,3)
model = viewer.draw DISK(1,32) # note the trick: angle == -u
###
#---------------------------------------------------

helicoid = (radius=1, h=1, turns=6, n=180, m=1) ->
	domain = SIMPLEXGRID [REPEAT(n)(turns*2*Math.PI/n), REPEAT(m)(radius/m)]
	fx = ([u,v]) -> v*Math.sin(u)
	fy = ([u,v]) -> v*Math.cos(u)
	fz = ([u,v]) -> u * h/(turns*2*Math.PI)
	object = MAP([fx, fy, fz])(domain)
	
model = viewer.draw helicoid(radius=1, h=3, turns=6, n=180, m=3)
##
#---------------------------------------------------
##
solidHelicoid = (width=0.1, radius=1, h=1, turns=6, n=180, m=1, p=1) ->
	domain = SIMPLEXGRID [REPEAT(n)(turns*2*Math.PI/n), REPEAT(m)(radius/m), REPEAT(p)(1/p)]
	fx = ([u,v,w]) -> v * Math.sin(-u)
	fy = ([u,v,w]) -> v * Math.cos(-u)
	fz = ([u,v,w]) -> width*w + (u * h/(turns*2*Math.PI))
	object = MAP([fx, fy, fz])(domain)
	
model = viewer.draw solidHelicoid(width=0.05, radius=1, h=3)
##
#---------------------------------------------------
