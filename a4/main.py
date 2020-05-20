from animals2 import *
from shapes2 import *

print("\n---------------------------------ANIMALS-------------------------------------\n")
print("DOG")
d = dog("sam","pomerian", 5, "male")
d.eating()
d.speak()
print(d.get_type())
print("Legs:{}".format(d.legs))
print("Eyes:{}".format(d.eyes))


print("\n")

print("CAT")
c = cat("rosie","white", 3, "female")
c.eating()
c.speak()
c.get_type()
print("Legs:{}".format(c.legs))
print("Eyes:{}".format(c.eyes))

print("\n")

print("COW")
w = cow("mel","white",12,"Female")
w.eating()
w.speak()
w.get_type()
print("Legs:{}".format(w.legs))
print("Eyes:{}".format(w.eyes))

print("\n")

print("PIG")
p = pig("ari","female",12,23)
p.eating()
p.speak()
p.get_type()
print("Legs:{}".format(p.legs))
print("Eyes:{}".format(p.eyes))

print("\n")

print("GIRAFFE")
g = giraffe("judy","female",5,4)
g.eating()
g.speak()
g.get_type()
print("Legs:{}".format(g.legs))
print("Eyes:{}".format(g.eyes))

print("\n")

print("LION")
l = lion("jack","male",11,180)
l.eating()
l.speak()
l.get_type()
print("Legs:{}".format(l.legs))
print("Eyes:{}".format(l.eyes))


print("\n")

print("DEER")
b = deer("jay","male",2,"False")
b.eating()
b.speak()
b.get_type()
print("Legs:{}".format(b.legs))
print("Eyes:{}".format(b.eyes))


print("\n")

print("HORSE")
h = horse("sky","white", 8, "male")
h.eating()
h.speak()
h.get_type()
print("Legs:{}".format(h.legs))
print("Eyes:{}".format(h.eyes))


print("\n")

print("MONKEY")
m = monkey("mia","new world monkey", 10, "female")
m.eating()
m.speak()
m.get_type()
print("Legs:{}".format(m.legs))
print("Eyes:{}".format(m.eyes))

print("\n")

print("TIGER")
t=tiger("ray",11, "male","True")
t.eating()
t.speak()
t.get_type()
print("Legs:{}".format(t.legs))
print("Eyes:{}".format(t.eyes))

print("\n---------------------------------SHAPES----------------------------------------\n")

print("TRIANGLE")
triangle = Triangle(3, 4, 5)
print("triangle sides:", triangle.sides)
print("triangle perimeter:", triangle.perimeter())
print("triangle area:", triangle.area(5,2))

print("\n")

print("RECTANGLE")
rectangle = Rectangle(4, 2)
print("rectangle sides:", rectangle.sides)
print("rectangle perimeter:", rectangle.perimeter())
print("rectangle area:", rectangle.area(5,2))

print("\n")

print("SQUARE")
square = Square(2)
print("square sides:", square.sides)
print("square perimeter:", square.perimeter())
print("square area:", square.area(5))

print("\n")

print("CIRCLE")
circle = Circle(3)
print("circle sides:", circle.sides)
print("circle perimeter:", circle.perimeter(3))
print("circle area:", circle.area(3))

print("\n")

print("PENTAGON")
pentagon = Pentagon(5)
print("pentagon sides:", pentagon.sides)
print("pentagon perimeter:", pentagon.perimeter())
print("pentagon area:", pentagon.area(5))

print("\n")

print("HEXAGON")
hexagon = Hexagon(6)
print("hexagon sides:", hexagon.sides)
print("hexagon perimeter:", hexagon.perimeter())
print("hexagon area:", hexagon.area(5))

print("\n")

print("OCTAGON")
octagon = Octagon(8)
print("octagon sides:", octagon.sides)
print("octagon perimeter:", octagon.perimeter())
print("octagon area:", octagon.area(5))

print("\n")

print("PARALELLOGRAM")
paralellogram = Paralellogram(2,4)
print("paralellogram sides:", paralellogram.sides)
print("paralellogram perimeter:", paralellogram.perimeter())
print("paralellogram area:", paralellogram.area(2,5))

print("\n")

print("TRAPEZIUM")
trapezium = Trapezium(1,2,3,4)
print("trapezium sides:", trapezium.sides)
print("trapezium perimeter:", trapezium.perimeter())
print("trapezium area:", trapezium.area(1,3,5))

print("\n")

print("RHOMBUS")
rhombus = Rhombus(5)
print("rhombus sides:", rhombus.sides)
print("rhombus perimeter:", rhombus.perimeter())
print("rhombus area:", rhombus.area(5,7))







