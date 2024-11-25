
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

action=input("Choose action: (+, -, *, /): ")

if action == "+":
    result = num1+num2
elif action == "-":
    result = num1 - num2
elif action == "*":
    result = num1 * num2
elif action == "/":
    if num2 == 0:
        result = "Unable division by zero!"
    else:
        result = num1 / num2

else:
    result = "Invalid input!"

print ("The result is: ", result)