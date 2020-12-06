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

    print(passport)
    passport_keys = passport.keys()

    if len(passport_keys) < 7:
        return False

    elif (len(passport_keys) == 8) or (len(passport_keys) == 7 and "cid" not in passport_keys):

        for key, value in passport.items():

            if key == 'byr' and (len(value) != 4 or (int(value) < 1920 or int(value) > 2002)):
                return False
            
            elif key == 'iyr' and (len(value) != 4 or (int(value) < 2010 or int(value) > 2020)):
                return False

            elif key == 'eyr' and (len(value) != 4 or (int(value) < 2020 or int(value) > 2030)):
                return False
            
            elif key == 'hgt':
                
                if ('cm' in value):
                    
                    height = int(value[:len(value) - 2])
                    
                    if (height < 150 or height > 193):
                        return False

                elif ('in' in value):
                    height = int(value[:len(value) - 2])

                    if (height < 59 or height > 76):
                        return False
                
                else:
                    return False
            
            elif key == 'hcl':
                
                if value[0] != '#' or len(value) !=7:

                   return False

                if not value[1:].isalnum():

                    return False

            elif key == 'ecl' and (value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):

                return False
            
            elif key == 'pid' and (len(value) != 9):

                return False

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

    # print(passports, len(passports))

    print(validate_passports(passports))


