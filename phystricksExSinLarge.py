from phystricks import *
def ExSinLarge():
    pspict,fig = SinglePicture("ExSinLarge")

    x=var('x')
    a=0
    b=pi
    f1=phyFunction(sin(x)+1).graph(a,b)
    f2=phyFunction(sin(x)+2).graph(a,b)

    surface=SurfaceBetweenFunctions(f1,f2)
    surface.parameters.color="red"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="blue"
    surface.curve2.parameters=surface.curve1.parameters

    pspict.DrawGraphs(surface)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
