
total_sum = 0

while True:
    user_input = input("Enter a positive number (or 'sum' to finish): ")

    if user_input.lower() == "sum":
        break

    try:
        num = float(user_input)
        if num > 0:
            total_sum += num;
    except Exception:
        print("Please enter number.")

print("The sum of positive numbers is:", total_sum)