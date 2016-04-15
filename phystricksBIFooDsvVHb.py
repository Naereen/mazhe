# -*- coding: utf8 -*-
from phystricks import *
def BIFooDsvVHb():
    pspict,fig = SinglePicture("BIFooDsvVHb")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(2)

    O=Point(0,0)
    cercle=Circle(  O,1 )
    P=cercle.get_point(60)
    Y=Point(0,P.y)
    X=Point(P.x,0)

    X.put_mark(0.2,-90,"\( x\)",automatic_place=(pspict,"N"))
    Y.put_mark(0.2,180,"\( y\)",automatic_place=(pspict,"E"))

    angle=Angle(X,O,P)
    angle.put_mark(0.2,angle.advised_mark_angle(pspict),"\( \\theta\)",automatic_place=(pspict,"corner"))

    seg=Segment(O,P)
    l1=Segment(P,X)
    l2=Segment(P,Y)

    l1.parameters.style="dashed"
    l2.parameters.style="dashed"

    pspict.DrawGraphs(cercle,angle,X,Y,seg,l1,l2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()