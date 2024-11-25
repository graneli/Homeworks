num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))

operator = input("Enter desired operator from the list (+, -, *, /): ")

operations_dict = {
    '+': num1+num2,
    '-': num1-num2,
    '*': num1*num2,
    '/': num1/num2 if num2 !=0
        else "Can't divide by zero"
}
if operator in operations_dict:
    result = operations_dict [operator]
else:
    result = "Entered operator is not in list"

print("Result is: ", result)