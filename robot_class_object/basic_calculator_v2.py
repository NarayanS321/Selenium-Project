class Calculator:

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model

    def get_calculator_details(self):
        details = (self.name, self.make, self.model)
        return details

    def addition(self, x, y):
        print("inside addition self = : ", self)
        sum1 = x + y
        return sum1

    @staticmethod
    def subtraction(x, y):
        sub1 = x - y
        return sub1

    @staticmethod
    def multiplication(x, y):
        return x * y

    def division(self, a, b):
        res = a / b
        return res

