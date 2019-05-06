import turtle    #importing turtle library

"""making a shape Class having a draw and initializing function"""


class Shape():
    def __init__(self):
        self.turtle=turtle.Pen()     #Making a turtle object.

    def draw(self):
        pass

"""making a 2d shape class inheriting it from shape class"""

class Shape_2d(Shape):
    def move(self,x,y):  #Defining a movee function to move shapes at different locations
        turtle.setheading(0)
        turtle.penup()

        turtle.setx(0.0)
        turtle.sety(0.0)
        turtle.goto(x, y)
        turtle.pendown()

    def draw(self):
        pass

"""making Rectangle Class inhereted from shape_2d Class"""


class Rectangle(Shape_2d):

    def __init__(self,length,height): # __init__ definition according to a rectangle
        self.length=length  #declaring length and height attribute of the rectangle
        self.height=height


    def draw(self):    #Drawing Rectangle using Turtle Library object

        super().move(200.0,0.0)  #using move function of the super class to define position of rectangle
        turtle.write('Rectangle')
        for j in range(0, 2):
            turtle.left(90)
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.height)

#=========================================================
"""making Square Class inhereted from Rectangle Class"""


class Square(Rectangle):

    def __init__(self,length): #defining __init__ defination according to a square
        super().__init__(length,length)

    def draw(self):

        super().move(0.0, 0.0) #using move function of the super class to define position of  square
        turtle.write('Square')
        for i in range(0, 4):
            turtle.forward(self.length)
            turtle.left(90)
#=============================================

"""making Circle Class inhereted from shape_2d Class"""


class Circle(Shape_2d):

    def __init__(self,radius): # __init__ definition according to a Circle
        self.radius=radius

    def draw(self):          #Drawing Circle using Turtle Library object inhereted from the super class of Shape class

        super().move(-120.0, 0.0) #using move function of the super class to define position of the circle
        turtle.write('Circle')
        turtle.circle(self.radius)

#====================================================
"""making Circle Equilateral Triangle inhereted from shape_2d Class"""


class Equilateral_triangle(Shape_2d):
    def __init__(self,length):  #Defining __init__according to a Equilateral triangle
        self.length=length

    # Drawing Equilateral Triangle using Turtle Library object inhereted from the super class of Shape class
    def draw(self):
        super().move(0.0,-150)    #using move function of the super class to define position of Equilateral triangle
        turtle.write('Equilteral Triangle', align='right')
        turtle.forward(self.length)
        for i in range(0, 2):
           turtle.left(120)
           turtle.forward(self.length)

#=================================================================


class Obtuse_triangle(Shape_2d):

    def __init__(self,length,hyp,angle): #Defining __init__ function according to a Obtuse triangle
        self.length=length
        self.hypotenuse=hyp
        self.angle=angle

    def draw(self): #Drawing Obtuse Triangle using Turtle Library object inhereted from the super class of Shape class

        super().move(-100.0, -100.0) #using move function of the super class to define position of Obtuse triangle

        turtle.write('Obtuse Triangle', align='right')
        turtle.forward(self.length)
        turtle.right(self.angle)
        turtle.backward(self.length)
        turtle.right((180-self.angle)/2)
        turtle.forward(self.hypotenuse)

#===================================================================


class Isosecles_triangle(Shape_2d):

    def __init__(self,length):  #Defining __init__ function according to a Isosecles triangle
        import math
        self.base=length
        self.perpendicular=length
        self.hypotenuse=math.sqrt((int(self.base)*(self.base))*2)

    # Drawing Isosceles Triangle using Turtle Library object inherited from the super class of Shape class
    def draw(self):

        super().move(200.0, -200.0) #using move function of the super class to define position of Isosceles triangle

        turtle.write('Isosceles Triangle', align='right')
        turtle.forward(self.base)
        turtle.right(45)
        turtle.backward(self.hypotenuse)
        turtle.right(45)
        turtle.forward(self.perpendicular)

#============================================================


rectangle_one=Rectangle(100,60)  #Making a rectangle object
rectangle_one.draw() #Calling draw method of rectangle to draw the rectangle

square_one=Square(100) #Making a Sqaure object
square_one.draw()

circle_one=Circle(100) #Making a Circle object
circle_one.draw()

equal_triangle_one=Equilateral_triangle(100)  #Making a Equilateral triangle object
equal_triangle_one.draw()

obtuse_triangle=Obtuse_triangle(100,175,120) #Making a Obtuse triangle object
obtuse_triangle.draw()

isosceles_triangle=Isosecles_triangle(100) #Making a Isosceles triangle object
isosceles_triangle.draw()
turtle.exitonclick()
