def find_highest_joltage(banks):
    total_joltage = 0
    for bank in banks:
        highest_ten = 0
        highest_unit = 0
        highest_ten_idx = 0
        for idx, digit in enumerate(bank[:-1]):
            if int(digit) > highest_ten:
                highest_ten = int(digit)
                highest_ten_idx = idx
        for digit in bank[highest_ten_idx+1:]:
            if int(digit) > highest_unit:
                highest_unit = int(digit)
        
        total_joltage += 10 * highest_ten + highest_unit

    return total_joltage


if __name__ == '__main__':

    with open("input.txt", "r", encoding="utf-8") as file:
        banks = [line.rstrip("\r\n") for line in file]

    total_joltage = find_highest_joltage(banks)

    print(total_joltage)
