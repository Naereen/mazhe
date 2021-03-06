from phystricks import *
def SurfacePrimiteGeog():
    pspict,fig = SinglePicture("SurfacePrimiteGeog")

    x=var('x')
    
    O = Point(0,0)
    mx = 1
    Mx = 5
    ms = 2
    Ms = 4
    f=phyFunction(3-2/x).graph(mx,Mx)
    f.parameters.color="red"
    A = f.get_point(ms)
    X = f.get_point(Ms)
    F = f.get_point(Mx)
    a = Point(ms,0)
    x = Point(Ms,0)
    N = Segment(X,x).center()


    surface=SurfaceUnderFunction(f,ms,Ms)
    surface.parameters.hatched()
    surface.parameters.hatch.color="blue"
    surface.Isegment.parameters.style="dashed"
    surface.Fsegment.parameters.style="dashed"

    a.put_mark(0.3,-90,"$a$",automatic_place=pspict)
    x.put_mark(0.3,-90,"$x$",automatic_place=pspict)
    F.put_mark(0.5,0,"$f(x)$",automatic_place=pspict)
    N.put_mark(2,0,"$S=F(x)=\int_a^xf(t)dt$",automatic_place=pspict)
    a.parameters.symbol=""
    x.parameters.symbol=""
    F.parameters.symbol=""
    N.parameters.symbol=""

    pspict.axes.no_graduation()

    pspict.DrawGraphs(f,surface,a,x,F,N,surface)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1.5)
    fig.conclude()
    fig.write_the_file()
