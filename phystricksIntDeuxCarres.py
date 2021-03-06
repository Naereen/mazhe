from phystricks import *
def IntDeuxCarres():
    pspict,fig = SinglePicture("IntDeuxCarres")

    c1=2
    c2=1
    rectangle1=Rectangle(Point(-c1,-c1),Point(c1,c1))
    rectangle2=Rectangle(Point(-c2,-c2),Point(c2,c2))

    rectangle1.parameters.hatched()
    rectangle1.parameters.hatch.color="green"
    rectangle1.parameters.color="red"

    rectangle2.parameters.color="red"
    rectangle2.parameters.filled()
    rectangle2.parameters.fill.color="white"

    pspict.DrawGraphs(rectangle1,rectangle2)

    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
