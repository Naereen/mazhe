# -*- coding: utf8 -*-
from phystricks import *
def EHDooGDwfjC():
    pspict,fig = SinglePicture("EHDooGDwfjC")
    pspict.dilatation_X(4)
    pspict.dilatation_Y(1)

    n=3
    A=Point(0,0)
    B=Point(1,0)
    C=Point(n,-n)

    K=Point(1,-1)

    AB=Segment(A,B)
    AC=Segment(A,C)

    d=Segment(C,B)
    parallel=d.fix_origin(K)
    L=Intersection( AB,parallel  )[0]

    KL=Segment(K,L)

    d.parameters.style="dashed"
    KL.parameters.style="dashed"

    A.put_mark(0.2,90,"\( A\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))
    K.put_mark(0.2,180+45,"\( K\)",automatic_place=(pspict,"corner"))
    L.put_mark(0.2,90,"\( L\)",automatic_place=(pspict,"S"))

    pspict.DrawGraphs(A,B,C,K,L,AB,AC,d,KL)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

