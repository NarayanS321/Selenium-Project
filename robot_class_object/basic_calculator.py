class Calculator:

    def __init__(self, name, make, model, x,y):
        self.name = name
        self.make = make
        self.model = model
        self.x = x
        self.y = y

    def get_calculator_details(self):
        details = (self.name, self.make, self.model)
        return details

    def get_addition(self):
        sum1 = self.x + self.y
        return sum1

    def get_subtraction(self):
        sub1 = self.x - self.y
        return sub1

    def get_multiplication(self):
        malt1 = self.x * self.y
        return malt1

    def get_division(self):
        div1 = self.x / self.y
        return div1



