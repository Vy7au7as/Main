def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
file_path = 'tekstas.txt'
gen = read_file(file_path)
for line in gen:
    print(line)
