from robot_class_object.geometrical_shape import Geometrical

class Square(Geometrical):

    def __init__(self, name, width, height):
        super().__init__(name)
        self.w = width
        self.h = height

    def get_area(self):
        area_sqr = self.w * self.h
        return area_sqr


