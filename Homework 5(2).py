import random

first_List = []
for number in range(20):
    first_List.append(random.randint (1,50))

print("This is FIrst list:",first_List)

list_odd = []
for num in first_List:
    if num % 2 != 0:
        list_odd.append(num)

print("Odd number list:", list_odd)

if len(list_odd) > 0:
    smallest = list_odd [0]
    largest = list_odd [0]

    for num in list_odd:
        if num < smallest:
            smallest=num
        if num > largest:
            largest = num

    print("Smalles odd number is:" , smallest)
    print("Largest odd number is:" , largest)

else:
    print("There are no odd numbers")
