def fibonacci(n):

    fibonacci_list = []

    for i in range(n):
        if i == 0:
            fibonacci_list.append(0)
        elif i == 1:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list

n = 8

print(fibonacci(n))

