def split_file(file):
    with open(file, 'r') as file:
        lines = file.readlines()

    for i in range(0, len(lines), 10):
        with open(f'file_part_{i//10 + 1}.txt', 'w') as part_file:
            part_file.writelines(lines[i:i+10])

split_file('file.txt')
