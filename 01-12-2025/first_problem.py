from utils import read_lines



def find_password(dial_setting, password, instructions):
    for instruction in instructions:
        if instruction[0] == 'R':
            dial_setting += int(instruction[1:])
            dial_setting = dial_setting % 100
            if dial_setting == 0:
                password += 1

        elif instruction[0] == 'L':
            dial_setting -= int(instruction[1:])
            dial_setting = dial_setting % 100
            if dial_setting == 0:
                password += 1
    return password

if __name__ == "__main__":

    dial_setting = 50
    password = 0
    
    instructions = read_lines("input.txt")
    print(find_password(dial_setting, password, instructions))