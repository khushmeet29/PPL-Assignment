import turtle
import math

class Rectangle:
    def __init__(self, len, wid):
        self.__length = len #Private Member
        self.__width = wid  #Private Member
   
    def get_side(self):
    	return (self.__length, self.__width )
       
    def set_side(self, len, wid):
        self.__length = len
        self.__width  = wid
        
    def get_perimeter(self):
        return (2*(self.__length + self.__width))
        
    def get_area(self):
        return (self.__length * self.__width)
   
    def draw(self):
        a = turtle.Turtle()
        a.forward(self.__length)
        a.left(90)
        a.forward(self.__width)
        a.left(90)
        a.forward(self.__length)
        a.left(90)
        a.forward(self.__width)
        a.left(90)

r = Rectangle(50,40)
print("Area of rectangle is ",r.get_area())
print("Perimeter of rectangle is",r.get_perimeter())
r.draw()

class square():
	def __init__(self, s):
		self.__side = s

	def get_side(self):
		return self.__side
		
	def set_side(self,s):
		self.__side = s
		
	def get_area(self):
		return (self.__side * self.__side)

	def get_perimeter(self):
		return (4 * self.__side)

	def draw(self):
		b = turtle.Turtle()
		b.forward(self.__side)
		b.left(90)
		b.forward(self.__side)
		b.left(90)
		b.forward(self.__side)
		b.left(90)
		b.forward(self.__side)
		b.left(90)

s = square(100)
s.draw()

class Triangle:
    def __init__(self, s1, s2, s3):
        self.side1 = s1   #Public Members
        self.side2 = s2
        self.side3 = s3
    
    def get_side(self):
        return (self.side1, self.side2, self.side3)
        
    def set_side(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def get_perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    
    def draw(self):
        c = turtle.Turtle()
        c.forward(self.side1)
        c.left(120)
        c.forward(self.side2)
        c.left(120)
        c.forward(self.side3)
 
t = Triangle(50,50,50)
print("Sides of triangle are:{}".format(t.get_side()))
t.draw()

class Circle:
    def __init__(self, r):
        self._radius = r #Protected Member
    
    def set_radius(self, r):
        self._radius = r
    
    def get_radius(self):
        return (self._radius)
    
    def get_area(self):
        pi = math.pi
        return (pi * self._radius * self._radius)
    
    def draw(self):
        d = turtle.Turtle()
        d.circle(self._radius)

c = Circle(25)
c.draw()

class Pentagon:
    def __init__(self, s):
        self.side = s #Public Member
    
    def set_side(self, s):
        self.side = s
        
    def get_side(self):
        return self.side 
    
    def draw(self):
       e = turtle.Turtle()
       for i in range(5):
            e.forward(self.side)
            e.right(72)
	
p = Pentagon(80)
print("Side of pentagon is:{}".format(p.get_side()))
p.draw()

class Hexagon:
    def __init__(self, s):
        self.side = s
    
    def set_side(self, s):
        self.side = s
    
    def draw(self):
        f = turtle.Turtle()
        for i in range(6):
            f.forward(self.side)
            f.right(60)

h = Hexagon(0)
h.set_side(100)
h.draw()

class Heptagon:
    def __init__(self, s):
        self.__side = s #Private Member
    
    def set_side(self, s):
        self.__side = s
    
    def get_side(self):
        return self.__side
    
    def draw(self):
        g = turtle.Turtle()
        for i in range(7):
            g.forward(self.__side)
            g.right(51.42)

h = Heptagon(100)
h.draw()

class Octagon:
    def __init__(self, s):
        self.__side = s #Private Member
    
    def set_side(self, s):
        self.__side = s
    
    def get_side(self):
        return self.__side
    
    def draw(self):
        h = turtle.Turtle()
        for i in range(8):
            h.forward(self.__side)
            h.right(45)

o = Octagon(100)
o.draw()

class Nanogon:
    def __init__(self, s):
        self.__side = s #Private Member
    
    def set_side(self, s):
        self.__side = s
    
    def get_side(self):
        return self.__side
    
    def draw(self):
        j = turtle.Turtle()
        for i in range(9):
            j.forward(self.__side)
            j.right(40)

n = Nanogon(100)
n.draw()

class Decagon:
    def __init__(self, s):
        self.__side = s #Private Member
    
    def set_side(self, s):
        self.__side = s
    
    def get_side(self):
        return self.__side
    
    def draw(self):
        k = turtle.Turtle()
        for i in range(10):
            k.forward(self.__side)
            k.right(36)
        turtle.done()

d = Decagon(100)
d.draw()


