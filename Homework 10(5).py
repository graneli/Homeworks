from functools import reduce

def multiply(numbers):
    try:
        result = reduce(lambda x, y: x * y, numbers)
        return {result}

    except TypeError:
        return "TypeError"

params = [1,2,3,4,5]
result = multiply(params)

print(result)
