from robot_class_object.pizza_making import Pizza

class PizzaFactory(Pizza):

    def make_pan_pizza(self):
        print(f"Your {self.type},{self.kind},{self.size} Pizza is Ready,enjoy your meal")

    def make_hand_made_pizza(self):
        print(f"Your {self.type},{self.kind},{self.size} Pizza is Ready,enjoy your meal")
