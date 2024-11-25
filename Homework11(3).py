def combine_files(file1, file, output_file):
    with open(file1, 'r') as f1, open(file, 'r') as f2, open(output_file, 'w') as out:
        out.write(f1.read())
        out.write(f2.read())

    with open(output_file, 'r') as combined:
        print(combined.read())

combine_files('file1.txt', 'file.txt', 'combined.txt')
