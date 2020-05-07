from robot_class_object.basic_calculator_v2 import Calculator

basic_cal1 = Calculator("BASIC", "CASIO", "CA101")
#basic_cal2 = Calculator("BASIC", "CASIO", "CA102")

print("basic cal : ", basic_cal1)
#print("basic cal2 : ", basic_cal2)

print()
print(" Sum = ", basic_cal1.addition(12, 8))
#print(" Sum = ", basic_cal2.addition(30, 8))
print()
print("Subtraction = ", basic_cal1.subtraction(30, 8))
print("Through static method Subtraction = ", Calculator.subtraction(30, 8))
