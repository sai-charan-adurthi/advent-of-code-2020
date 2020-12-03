import fileinput

input_list = []

count = 0

for line in fileinput.input():
    input_list.append(line.strip())

x = 0

for i in range(1, len(input_list)):

    row = input_list[i]
    x = (x + 3) % len(row)
    
    if row[x] == '#':
        count += 1

    i += 1

print(count)