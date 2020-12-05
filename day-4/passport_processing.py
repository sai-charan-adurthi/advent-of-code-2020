
def parse_file(filename):
    passport_data = []
    
    with open(filename, "r") as file:

        passport = dict()
        for line in file.readlines():
            if line == "\n":
                passport_data.append(passport)
                passport = dict()
                continue
            
            temp = []

            temp = line.strip().split(' ')

            for ele in temp:
                
                key, val = ele.split(':')
                passport[key] = val

        passport_data.append(passport)  

    return passport_data

def validate_passport(passport):

    passport_keys = passport.keys()

    if len(passport_keys) < 7 :
        return False
    
    elif len(passport_keys) == 7 and "cid" not in passport_keys:
        return True
    
    elif len(passport_keys) == 8:
        return True
    
    else:
        return False
    
def validate_passports(passport_data):

    count = 0

    for passport in passport_data:

        if validate_passport(passport):
            count += 1
    
    return count

if __name__ == "__main__":
    passports = parse_file("day-4/input.txt")

    print(passports, len(passports))

    print(validate_passports(passports))