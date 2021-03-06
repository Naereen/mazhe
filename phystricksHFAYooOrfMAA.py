# -*- coding: utf8 -*-
from phystricks import *
def HFAYooOrfMAA():
    pspict,fig = SinglePicture("HFAYooOrfMAA")
    C=Point(0,0.5)
    alpha=0
    circle = Circle(C,0.5)

    c1=circle.graph(-90,alpha)
    c2=circle.graph(alpha,270)
    c1.parameters.color="red"
    c2.parameters.color="blue"
    P=circle.get_point(alpha)
    P.put_mark(0.3,-45,"$P$",automatic_place=pspict)

    s1=Segment(Point(0,0),P)
    segment=s1.dilatation(2)
    segment.parameters.color="red"

    surface=SurfaceBetweenParametricCurves(  s1,circle,(0,s1.length()) , (-pi/2,radian(alpha)) )
    surface.parameters.filled()
    surface.parameters.fill.color="cyan"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.curve2.parameters=surface.curve1.parameters

    pspict.DrawGraphs(c1,c2,surface,segment,P)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.dilatation(2)
    fig.conclude()
    fig.write_the_file()
