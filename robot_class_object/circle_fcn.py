from robot_class_object.geometrical_shape import Geometrical
import math


class Circle(Geometrical):

    def __init__(self, name, radius):
        self.r = radius
        super().__init__(name)
        self.PI = 3.14

    def get_area(self):
        # area_cir = self.PI * (self.r **2)
        area_cir = self.PI * (math.pow(self.r, 2))
        print(f"Area of {self.name} is : {area_cir}")
