def parse_file(filename):
    map = []
    with open(filename, "r") as file:
        for line in file.readlines():
            map.append(line.strip())
    return map

def count_trees_in_slope(map, deltaX, deltaY):
    x = 0
    y = 0
    count = 0

    for i in range(deltaY, len(map), deltaY):
        y = i 
        row = map[y]
        x = (x + deltaX) % len(row)
        
        # print(f"{y} x {x} : {row[x]}")

        if row[x] == '#':
            count += 1
    
    return count


def count_trees_on_multi_slope(map, slopes):
    product = 1
    for slope in slopes:
        product *= count_trees_in_slope(map, slope[0], slope[1])
    return product

if __name__ == "__main__":
    map = parse_file("day-3/input.txt")
    test_map = parse_file("day-3/test_input.txt")
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(f"336=={count_trees_on_multi_slope(test_map, slopes)}")
    # print(f"?=={count_trees_on_multi_slope(map, slopes)}")
    print(f"?=={count_trees_on_multi_slope(map, slopes)}")
