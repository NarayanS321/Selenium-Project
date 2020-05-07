from robot_class_object.squrae_fcn import Square
from robot_class_object.triangle_fcn import Tringle
from robot_class_object.circle_fcn import Circle

cir1 = Circle("circle", 10)
cir1.get_area()
print()
tri1 = Tringle("triangle",10,15)
print(f"Area of Triangle is {tri1.get_area()}")
print()
squ1 = Square("squre",15,25)
print(f"Area of Square is {squ1.get_area()}")

