my_list = [43, '22', 12, 66, 210, ["hi"]]

ind210 = my_list.index(210)
print("Index of 210 is:", ind210)

my_list.append("hello")
print("Here is list , with added last element", my_list)

del my_list[2]
print("List after deleting index 2 element:",my_list)

my_list_2 = my_list.copy()
my_list_2.clear()

print("My list:", my_list)
print("My list after clearing:", my_list_2)



