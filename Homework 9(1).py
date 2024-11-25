int_list = [10,20,30,40]

def add_to_list(number):
    global int_list
    int_list.append(number)

add_to_list(input("Enter Desired number: "))
print(int_list)