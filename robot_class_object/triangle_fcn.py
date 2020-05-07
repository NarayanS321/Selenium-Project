from robot_class_object.geometrical_shape import Geometrical

class Tringle(Geometrical):

    def __init__(self,name,base,height):
        super().__init__(name)
        self.b = base
        self.h = height

    def get_area(self):
        area_trg = (self.b * self.h) / 2
        return area_trg
