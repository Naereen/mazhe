# -*- coding: utf8 -*-
from phystricks import *

def YWxOAkh():
    pspict,fig = SinglePicture("YWxOAkh")

    x=var('x')
    epsilon=0.005
    mx=epsilon
    Mx=0.5
    f2=phyFunction(sin(1/x))
	#pts = Intersection(f1,f2)
	#x0=pts[0].x
    x0=epsilon
    x1=1
    #F1=f1.graph(x1,Mx)
    F2=f2.graph(x0,Mx)
    F2.parameters.plotpoints=5000
    #F1.parameters.color="gray"
    #F1.parameters.style="dashed"
    #F2.parameters=F1.parameters
    #F1p=f1.graph(-Mx/2,-mx)
    F2p=f2.graph(-Mx/2,-mx)
    F2p.parameters.plotpoints=F2.parameters.plotpoints
    #F1p.parameters=F1.parameters
    #F2p.parameters=F1.parameters
    
    #P=Point(0,0.7)
    #Cer=Circle(P,0.1)
    
    #A=SurfaceBetweenFunctions(f1,f2,x0,x1)
    #A.f2.parameters.plotpoints=F2.parameters.plotpoints
    #A.vertical_left.parameters.style="solid"
    #A.vertical_left.parameters.color="blue"
    #A.vertical_right.parameters = A.vertical_left.parameters
    #A.parameters.hatched()
    #A.parameters.hatch.color="red"
    #A.f1.parameters.color="blue"
    #A.f1.parameters.style="solid"
    #A.f2.parameters = A.f1.parameters
    
    pspict.DrawGraphs(F2)
	#pspict.DrawGraphs(F1p,F2p,F1,F2,P)
    
    pspict.axes.Dx=0.5
    pspict.DrawDefaultAxes()
    pspict.dilatation_X(4)
    
    fig.conclude()
    fig.write_the_file()
