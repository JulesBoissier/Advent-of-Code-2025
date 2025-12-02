def find_invalid_ids(id_ranges):
    invalid_ids = []
    for id_range in id_ranges:
        low = int(id_range.split('-')[0])
        high = int(id_range.split('-')[1]) + 1

        for id in range(low, high):
            id_string = str(id)

            if len(id_string) % 2 == 1:
                continue

            pattern_length = int(len(id_string)/2)
            first_half = id_string[:pattern_length]
            second_half = id_string[pattern_length:]

            if second_half[0] == '0':
                continue
            elif first_half == second_half:
                invalid_ids.append(id)

        
    return sum(invalid_ids)

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        content = f.read().strip("\r\n")
    id_ranges = [item for item in content.split(",") if item]        

    id_sum = find_invalid_ids(id_ranges)

    print(id_sum)