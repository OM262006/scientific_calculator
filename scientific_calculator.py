import math


num1 = float(input("enter num1:"))
num2 = float(input("enter num2:"))

op  = input("chose one oprator +,-,*,%,/,**:")

if op == "+":
    print("sum of  num1 and num2 is:", num1 + num2)
elif op == "-":
    print("sub of num1 and num2 is:", num1 - num2)
elif op == "*":
    print("mult of num1 and num2 is:", num1 * num2)
elif op == "/":
    print("divi of num1 and num2 is:", num1 / num2)
elif op == "%":
    print("modlus of num1 and num2 is:", num1 % num2)
elif op == "**":
    print("power of num1 and num2:", num1 ** num2)
else:
    print("invalid op",op)