import math
from abc import ABC, abstractmethod

class Shape(ABC): #Parent Class(Abstract Class)
	sides = None

	def __init__(self, sides):
		self.sides = sides
		
	@abstractmethod
	def perimeter(self): #Virtual Function
		pass
		
	@abstractmethod        
	def area(self): #Virtual Function
		pass

class Triangle(Shape): #Child Class 
	def __init__(self, side1, side2, side3):
		self.sides = [side1, side2, side3]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
        
	def area(self,side3,height): #Function Overloading
		area = 0.5*side3*height
		return area
	
class Rectangle(Shape): #Child Class
	def __init__(self, length, width):
		self.sides = [length, width, length, width]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,length,width): #Function Overloading
		area = length*width
		return area

class Square(Shape): #Child Class
	def __init__(self, side):
		self.sides = [side, side, side, side]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,side): #Function Overloading
		area = side*side
		return area
        
class Circle(Shape): #Child Class
	def __init__(self, side):
		self.sides = [side]
        
	def perimeter(self,side): #Method Overriding(Polymorphism)
		perimeter = 2*(math.pi)*(side)        
		return perimeter
        
	def area(self,side): #Function Overloading
		area = (math.pi)*side*side
		return area
        
class Pentagon(Shape): #Child Class
	def __init__(self, side):
		self.sides = [side, side, side, side,side]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,side): #Function Overloading
		area = ((math.sqrt(5*(5+2*math.sqrt(5))))*side*side)/4
		return area
        
class Hexagon(Shape): #Child Class
	def __init__(self, side):
		self.sides = [side, side, side, side, side, side]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,side): #Function Overloading
		area = (3*math.sqrt(3)*side*side)/2
		return area
        
class Octagon(Shape): #Child Class
	def __init__(self, side):
		self.sides = [side, side, side, side, side, side, side, side]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,side): #Function Overloading
		area = 2*(1+math.sqrt(2))*side*side
		return area
        
class Paralellogram(Shape): #Child Class
	def __init__(self, side1,side2):
		self.sides = [side1, side2, side1, side2]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,side1,height): #Function Overloading
		area = side1*height
		return area
        
class Trapezium(Shape): #Child Class
	def __init__(self, side1,side2,side3,side4):
		self.sides = [side1, side2, side3, side4]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,side1,side3,height): #Function Overloading
		area = ((side1+side3)*height)/2
		return area
        
class Rhombus(Shape):
	def __init__(self, side): #Child Class
		self.sides = [side, side, side, side]
        
	def perimeter(self):
		perimeter=0
		for side in self.sides:
			perimeter += side
		return perimeter
    
	def area(self,side,height): #Function Overloading
		area = side*height
		return area
        

