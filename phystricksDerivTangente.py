from phystricks import *
def DerivTangente():
	pspict,fig = SinglePicture("DerivTangenteOM")

	a=3
	xb=6.5
	mx=1
	Mx=7
	x=var('x')
	f=phyFunction((x/3)**3/2+1).graph(mx,Mx)
	A=f.get_point(a)
	Ax=Point(A.x,0)
	Ay=Point(0,A.y)
	X=f.get_point(xb)
	Xx=Point(X.x,0)
	Xy=Point(0,X.y)
	
	Ay.put_mark(0.1,180,"$f(a)$",automatic_place=(pspict,"E"))
	Xy.put_mark(0.1,180,"$f(x)$",automatic_place=(pspict,"E"))
	Ax.put_mark(0.2,-90,"$a$",automatic_place=(pspict,"N"))
	Xx.put_mark(0.2,-90,"$x$",automatic_place=(pspict,"N"))

	v1=Segment(X,Xx)
	v2=Segment(A,Ax)
	h1=Segment(X,Xy)
	h2=Segment(A,Ay)
	I=Intersection(v1,h2)[0]
	h3=Segment(A,I)
	v1.parameters.color="green"
	v1.parameters.style="dashed"
	v2.parameters=v1.parameters
	h1.parameters=v1.parameters
	h2.parameters=v1.parameters
	h3.parameters=v1.parameters

	corde=Segment(A,X).dilatation(1.5)
	corde.parameters.color="cyan"

	Dx=MeasureLength(h3,0.2)
	#Dx.put_mark(0.2,-90,"$\Delta x$",automatic_place=(pspict,"N"))
	Dx.put_mark(0.2,-90,"$x-a$",automatic_place=(pspict,"N"))
	Dy=MeasureLength(Segment(X,I),-0.2)
	#Dy.put_mark(0.2,0,"$\Delta y$",automatic_place=(pspict,"W"))
	Dy.put_mark(0.2,0,"$f(x)-f(a)$",automatic_place=(pspict,"W"))

	pspict.DrawGraphs(corde,v1,v2,h1,h2,h3,f,A,Ax,Ay,X,Xx,Xy,Dx,Dy)

	pspict.axes.no_graduation()
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
