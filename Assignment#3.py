import turtle
"""making a shape Class having a draw and initializing function"""


class Shape():
    def __init__(self):
        pass
    def draw(self):
        pass

"""making a 2d shape class inheriting it from shape class"""

class Shape_2d(Shape):
    def draw(self):
        pass

"""making Rectangle Class inhereted from shape_2d Class"""


class Rectangle(Shape_2d):

    def __init__(self,length,height,angle): #changing __init__ defination according to a rectangle
        self.length=length
        self.height=height
        self.angle=angle

    def draw(self):    #Drawing Rectangle using Turtle Library object
        import turtle
        t=turtle.Pen()
        t.penup()
        t.goto(220.0,0.0)
        t.pendown()
        t.write('Rectangle')
        for j in range(0, 2):
            t.left(self.angle)
            t.forward(self.length)
            t.left(self.angle)
            t.forward(self.height)

#=========================================================
"""making Square Class inhereted from Rectangle Class"""


class Square(Rectangle):

    def __init__(self,length,angle): #changing __init__ defination according to a square
        self.length=length
        self.angle=angle

    def draw(self):              #Drawing Square using Turtle Library object
        import  turtle
        q=turtle.Pen()
        q.pendown()
        q.write('Square')
        for i in range(0, 4):
            q.forward(self.length)
            q.left(self.angle)
#=============================================

"""making Circle Class inhereted from shape_2d Class"""


class Circle(Shape_2d):

    def __init__(self,radius): #changing __init__ defination according to a Circle
        self.radius=radius

    def draw(self):          #Drawing Circle using Turtle Library object
        import turtle
        c=turtle.Pen()
        c.penup()
        c.goto(-120.0, 0.0)
        c.pendown()
        c.write('Circle')
        c.circle(self.radius)

#====================================================
"""making Circle Equilateral Triangle inhereted from shape_2d Class"""


class Equilateral_triangle(Shape_2d):
    def __init__(self,length,angle):
        self.length=length
        self.angle=angle

    def draw(self):
        import turtle
        equilateral_triangle = turtle.Turtle()
        equilateral_triangle.penup()
        equilateral_triangle.goto(0.0, -100.0)
        equilateral_triangle.write('Equilteral Triangle', align='right')
        equilateral_triangle.pendown()
        equilateral_triangle.forward(100)
        for i in range(0, 2):
            equilateral_triangle.left(120)
            equilateral_triangle.forward(100)

#=================================================================


class Obtuse_triangle(Shape_2d):

    def __init__(self,length,hyp,angle):
        self.length=length
        self.hypotenuse=hyp
        self.angle=angle

    def draw(self):
        import turtle
        obtuse_triangle = turtle.Turtle()
        obtuse_triangle.penup()
        obtuse_triangle.goto(0.0, 150.0)
        obtuse_triangle.pendown()
        obtuse_triangle.write('Obtuse Triangle', align='left')
        obtuse_triangle.forward(self.length)
        obtuse_triangle.right(self.angle)
        obtuse_triangle.backward(self.length)
        obtuse_triangle.right((180-self.angle)/2)
        obtuse_triangle.forward(self.hypotenuse)

#===================================================================


class Isosecles_triangle(Shape_2d):

    def __init__(self,length):
        import math
        self.base=length
        self.perpendicular=length
        print()
        print((int(self.base)^2*2))
        self.hypotenuse=math.sqrt((int(self.base)*(self.base))*2)

    def draw(self):
        import turtle
        isosceles_triangle = turtle.Turtle()
        isosceles_triangle.penup()
        isosceles_triangle.goto(-150.0, -150.0)
        isosceles_triangle.pendown()
        isosceles_triangle.write('Isosceles Triangle', align='right')
        isosceles_triangle.forward(self.base)
        isosceles_triangle.right(45)
        isosceles_triangle.backward(self.hypotenuse)
        isosceles_triangle.right(45)
        isosceles_triangle.forward(self.perpendicular)

#============================================================


rectangle_one=Rectangle(100,60,90)
rectangle_one.draw()

square_one=Square(100,90)
square_one.draw()

circle_one=Circle(100)
circle_one.draw()

equal_triangle_one=Equilateral_triangle(100,120)
equal_triangle_one.draw()

obtuse_triangle=Obtuse_triangle(100,175,120)
obtuse_triangle.draw()

isosceles_triangle=Isosecles_triangle(100)
isosceles_triangle.draw()
turtle.exitonclick()