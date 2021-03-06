# -*- coding: utf8 -*-
from phystricks import *
def UYJooCWjLgK():
    pspict,fig = SinglePicture("UYJooCWjLgK")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(2)

    x=3
    y=2
    theta=30
    A=Point(0,0)

    Y=Circle(A,y).get_point(theta)
    P=Circle(A,1).get_point(theta)
    X=Point(x,0)
    d1=Segment(A,Y)
    d2=Segment(A,X)

    s=Segment(P,X)
    sp=s.fix_origin(Y)
    B=Intersection( sp,d2 )[0]

    d2=Segment(A,B).dilatation(1.2)

    PX=Segment(P,X)
    YB=Segment(Y,B)

    PX.parameters.style="dashed"
    YB.parameters.style="dashed"

    A.put_mark(0.2,90+theta,"\( 0\)",automatic_place=(pspict,"corner"))
    Y.put_mark(0.2,90+theta,"\( y\)",automatic_place=(pspict,"corner"))
    P.put_mark(0.2,90+theta,"\( 1\)",automatic_place=(pspict,"corner"))
    X.put_mark(0.2,-90,"\( x\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"\( xy\)",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(d1,d2,A,Y,X,B,P,PX,YB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

