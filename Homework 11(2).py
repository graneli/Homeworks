def write_lines():
    with open('file.txt', 'w') as file:
        for i in range(1, 18):
            if i == 2:
                file.write("Line 2\n")
            elif i == 8:
                file.write("Line 8\n")
            elif i == 10:
                file.write("Line 10\n")
            elif i == 13:
                file.write("Line 13\n")
            elif i == 17:
                file.write("Line 17\n")
            else:
                file.write(f"{i}\n")


write_lines()
