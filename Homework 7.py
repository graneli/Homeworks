#Homework7(1)
squared_numbers = {x**2 for x in range(1, 11)}
print("Squared numbers:", squared_numbers)

#Homework7(2)
user_string = input("Enter a string: ")
character_set = set(user_string)
print("Set of characters:", character_set)

#Homework7(3)
tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

combined_tuple = tuple(set(tuple1 + tuple2))
duplicated_values = list(set(x for x in tuple1 if tuple2.count(x) > 0))

print("Combined tuple:", combined_tuple)
print("Duplicated values:", duplicated_values)

#Homework7(4)
tuple = (1, 2, 3, 4)
swapped_tuple = (tuple[-1],) + tuple[1:-1] + (tuple[0],)
print("Swapped tuple:", swapped_tuple)

#Homework7(5)
nested_tuple = (1, (2, 3), (4, (5, 6)))

def flatten_tuple(t):
    flat = []
    for item in t:
        if isinstance(item, tuple):
            flat.extend(flatten_tuple(item))
        else:
            flat.append(item)
    return tuple(flat)

flattened_tuple = flatten_tuple(nested_tuple)
print("Flattened tuple:", flattened_tuple)

#Homework7(6)
set1 = {1, 2}
set2 = {'a', 'b'}

combined = {(x, y) for x in set1 for y in set2}
print("Combined set of tuples:", combined)