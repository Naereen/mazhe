# -*- coding: utf8 -*-
from phystricks import *
def FGWjJBX():
    pspict,fig = SinglePicture("FGWjJBX")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,0)
    C=Point(2,0)
    D=Point(3,0)
    E=Point(4,0.5)
    F=Point(4,-0.5)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CD=Segment(C,D)
    DE=Segment(D,E)
    DF=Segment(D,F)

    BC.parameters.style='dotted'

    A.put_mark(0.2,90,"\( \\alpha_1\)",automatic_place=(pspict,"S"))
    B.put_mark(0.2,90,"\( \\alpha_2\)",automatic_place=(pspict,"S"))
    D.put_mark(0.2,90,"\( \\alpha_{l-2}\)",automatic_place=(pspict,"S"))
    E.put_mark(0.2,90,"\( \\alpha_{l-1}\)",automatic_place=(pspict,"S"))
    F.put_mark(0.2,90,"\( \\alpha_l\)",automatic_place=(pspict,"S"))

    pspict.DrawGraphs(AB,BC,CD,DE,DF,A,B,C,D,E,F)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
