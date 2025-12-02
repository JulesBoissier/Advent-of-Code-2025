from utils import read_lines



def find_password(dial_setting, password, instructions):
    for instruction in instructions:

        amount = int(instruction[1:])
        if amount >= 100:
            password += (amount // 100)
            amount = amount % 100

        if instruction[0] == 'R':
            dial_setting += amount
            if dial_setting >= 100:
                password += 1
                dial_setting -= 100

        else:
            was_not_at_zero = (dial_setting != 0)
            dial_setting -= amount

            if dial_setting < 0:
                if was_not_at_zero:
                    password += 1
                dial_setting +=  100
            elif dial_setting == 0:
                password += 1



    return password

if __name__ == "__main__":

    dial_setting = 50
    password = 0
    
    instructions = read_lines("input.txt")
    print(find_password(dial_setting, password, instructions))
