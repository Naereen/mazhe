# -*- coding: utf8 -*-
from phystricks import *
def LLVMooWOkvAB():
    pspict,fig = SinglePicture("LLVMooWOkvAB")
    x=var('x')
    f1=phyFunction(x)
    f2=phyFunction(x**2)

    surface=SurfaceBetweenFunctions(f1,f2,mx=0,Mx=1)
    surface.parameters.color="green"
    surface.curve2.put_arrow(0.5)
    surface.curve1.put_arrow(0.5)
    surface.curve1.record_arrows[0]=-surface.curve1.record_arrows[0]

    pspict.DrawGraphs(surface)
    pspict.DrawDefaultAxes()
    pspict.dilatation(3)
    fig.conclude()
    fig.write_the_file()
