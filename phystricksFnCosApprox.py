from phystricks import *
def FnCosApprox():
    pspict,fig = SinglePicture("FnCosApprox")

    x=var('x')
    f=phyFunction(cos(x)).graph(0,pi)
    P=f.get_point(pi/4)
    P.put_mark(0.15,P.advised_mark_angle(pspict),"$P$",automatic_place=pspict)
    pspict.axes.single_axeX.axes_unit=AxesUnit(pi,"")
    pspict.axes.single_axeX.Dx=0.25

    pspict.DrawGraphs(f,P)
    pspict.DrawDefaultAxes()
    pspict.dilatation(2)
    fig.conclude()
    fig.write_the_file()
