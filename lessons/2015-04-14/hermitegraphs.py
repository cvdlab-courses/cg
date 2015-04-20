
""" grafici base cubica di hermite """

def h1(u): return 2*u**3 -3*u**2 + 1
def h2(u): return -2*u**3 + 3*u**2
def h3(u): return u**3 -2*u**2 + u
def h4(u): return u**3 - u**2

dom = INTERVALS(1)(32)

def x(h):
	def x0(p): 
		return p[0]
	return x0
	
def y(h):
	def y0(p): 
		return h(p[0])
	return y0

AA(CONS([x,y]))([h1,h2,h3,h4])

VIEW(MAP([x(h1),y(h1)])(dom))

VIEW(STRUCT([
	MAP(CONS([x,y])(h1))(dom),
	MAP(CONS([x,y])(h2))(dom),
	MAP(CONS([x,y])(h3))(dom),
	MAP(CONS([x,y])(h4))(dom)
]))

AA(MAP)(AA(CONS([x,y]))([h1,h2,h3,h4]))

VIEW(STRUCT(CONS(AA(MAP)(AA(CONS([x,y]))([h1,h2,h3,h4])))(dom)))