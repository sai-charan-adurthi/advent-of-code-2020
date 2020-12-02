import fileinput

input_list = []

count = 0

for line in fileinput.input():

    words = line.split(': ')

    policy_data = words[0].split(' ')

    pos_1, pos_2 = map(int, policy_data[0].split('-'))

    print(pos_1, pos_2, policy_data[1], words[1])

    if words[1][pos_1-1] == policy_data[1]:
        if words[1][pos_2-1] != policy_data[1]:
            count += 1
            continue

    if words[1][pos_2-1] == policy_data[1]:
        if words[1][pos_1-1] != policy_data[1]:
            count += 1

print(count)