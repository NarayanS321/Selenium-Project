from robot_class_object.basic_calculator import Calculator
from robot_class_object.sci_fi_calculator import ScifiCalculator


calculator1 = Calculator("BASIC", "CASIO", "CA101", 10, 5)
calculator2 = ScifiCalculator("scifi","linux","sc202",10,15)



print()
print(f" My Calculator details are = {calculator1.get_calculator_details()}")
print()
print(f" total Addition = {calculator1.get_addition()}")
print()
print(f" total Subtraction = {calculator1.get_subtraction()}")
print()
print(f" total Multiplication = {calculator1.get_multiplication()}")
print()
print(f" total Division = {calculator1.get_division()}")
print()
print(f" My Calculator details are = {calculator2.get_calculator_details()}")
print()
print(f" total Square Root = {calculator2.get_square_root()}")



