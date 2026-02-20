# Simple Python Calculator
# num1 = input(int("Enter the first number": ))
# operator = input("Enter the operator(+,-,/,*):")
# num2 = input(int("Enter the second number":))
#   if operator = "+"
#      sum = num1 + num2; 
#      print("The sum of the two numbers is:", sum),
#   elif operator ="-";
#      diff = num1 - num2; 
#      print("The difference of the two numbers is:", diff),
#   elif operator = "/";
#        quotient = num1/num2; 
#        print("The quotient is:", quotient),
#   elif operator = "*";
#      prod = num1 * num2; Print("The product of the numbers is:", prod) 
#   else Print("Enter the right operator")







# Simple Python Calculator
# num1 = int(input("Enter the first number: " ))
# operator = input("Enter the operator(+,-,/,*) ")
# num2 = int(input("Enter the second number: "))
#if operator == "+":
#      sum = num1 + num2
#      print("The sum of the two numbers is:", sum)
#   elif operator =="-":
#      diff = num1 - num2
#      print("The difference of the two numbers is:", diff)
#   elif operator == "*":
#        prod = num1 * num2
#        print("The product of the numbers is:", prod) 
#   elif operator == "/":
         # if num2 != 0:
#             quotient = num1/num2
#             print("The quotient is:", quotient)
         # else:
              # print("Error: division by zero is not allowed")

#   else:
        # print("Enter the right operator")


# I don't even know what is wrong with this code anymore 😭😭














# Simple Python Calculator

num1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("The sum of the two numbers is:", result)

elif operator == "-":
    result = num1 - num2
    print("The difference of the two numbers is:", result)

elif operator == "*":
    result = num1 * num2
    print("The product of the numbers is:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("The quotient is:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Enter the right operator.")

