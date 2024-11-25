def sum_of_numbers (number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_numbers(number//10)

result=sum_of_numbers(int(input("Enter your numbers: ")))

print(result)