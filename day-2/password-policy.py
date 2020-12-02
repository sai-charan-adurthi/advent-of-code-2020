import fileinput

input_list = []

count = 0

for line in fileinput.input():

    # split the input
    words = line.split(': ')

    policy_data = words[0].split(' ')

    min_val, max_val = policy_data[0].split('-')

    print(min_val, max_val, policy_data[1], words[1])
    
    str_count = words[1].count(policy_data[1])

    if policy_data[1] in words[1] and ((str_count >= int(min_val)) and (str_count <= int(max_val))) :

        count += 1

print(count)
