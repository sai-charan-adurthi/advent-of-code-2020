import fileinput

input_list = []

for line in fileinput.input():
    input_list.append(int(line))

# print(input_list)
def print_pair_product(input_list):

    num_set = set()

    for i in range(0, len(input_list)):

        diff_val = 2020 - input_list[i]
        
        if (diff_val) in num_set:
            return (input_list[i]) * (diff_val) 
        num_set.add(input_list[i])
    
    return None

print(print_pair_product(input_list))

def print_triplet_product(input_list):

    for i in range(0, len(input_list)):

        num_set = set()
        diff_val = 2020 - input_list[i]

        for j in range(i + 1, len(input_list)):
            temp = diff_val - input_list[j]
            if (temp) in num_set:
                return (input_list[i] * input_list[j] * temp)
            
            num_set.add(input_list[j])

    return None

print(print_triplet_product(input_list))