from phystricks import *
def Bateau():
	pspict,fig = SinglePicture("Bateau")
	pspict.specific_needs="\usepackage[cdot,thinqspace,amssymb]{SIunits}"

	dA=2.5
	dB=4.5
	O=Point(0,0)
	A=Point(0,dA)
	B=Point(4,dB)
	Bp=Point(4,-dB)
	J=Point(4,0)
	K=Point(B.x,A.y)

	A.put_mark(0.3,90,"$A$",automatic_place=pspict)
	B.put_mark(0.3,90,"$B$",automatic_place=pspict)
	Bp.put_mark(0.3,-90,"$B'$",automatic_place=pspict)

	plage=Segment(O,J).dilatation(1.5)

	quatre=MeasureLength(Segment(A,K),0)
	quatre.put_mark(0.1,90,"$\unit{4}{\kilo\meter}$",automatic_place=(pspict,"S"))

	neuf=MeasureLength(Segment(B,J),-0.2)
	neuf.put_mark(0.1,0,"$\unit{9}{\kilo\meter}$",automatic_place=(pspict,"W"))

	trois=MeasureLength(Segment(A,O),0)
	trois.put_mark(0.1,180,"$\unit{3}{\kilo\meter}$",automatic_place=(pspict,"E"))

	I=Intersection( Segment(A,Bp),plage )[0]
	I.put_mark(0.3,45,"$I$",automatic_place=pspict)
	ixe=MeasureLength(Segment(O,I),0.2)
	ixe.put_mark(0.1,-90,"$x\kilo\meter$",automatic_place=(pspict,"N"))


	proj=Segment(B,Bp)
	proj.parameters.color="brown"
	proj.parameters.style="dashed"

	trajet=Segment(A,Bp)
	trajet.parameters.color="blue"
	trajet.parameters.style="dashed"

	pspict.DrawGraphs(plage,A,quatre,neuf,trois,I,proj,trajet,B,Bp,ixe,I)
	#pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
