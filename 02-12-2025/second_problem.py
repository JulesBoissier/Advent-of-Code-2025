def generate_factor_dict(id_string):

    factors_dict = dict()

    for length in range(1, len(id_string)): 
        if len(id_string) % length == 0: 
            factors_dict[length] = int(len(id_string) / length)
    
    return factors_dict

def find_invalid_ids(id_ranges):

    invalid_ids = []
    
    for id_range in id_ranges:
        low = int(id_range.split('-')[0])
        high = int(id_range.split('-')[1]) + 1

        for id in range(low, high):
            id_string = str(id)

            factors_dict = generate_factor_dict(id_string)

            for pattern_length in factors_dict.keys():
                list_of_subsets = []

                for i in range(factors_dict[pattern_length]):
                    pattern = id_string[i * pattern_length: (i+1) * pattern_length]
                    
                    list_of_subsets.append(pattern)
                

                if len(set(list_of_subsets)) == 1 and list_of_subsets[0][0] != '0':
                    invalid_ids.append(id)
                    break


    return sum(invalid_ids)

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        content = f.read().strip("\r\n")
    id_ranges = [item for item in content.split(",") if item]        

    id_sum = find_invalid_ids(id_ranges)

    print(id_sum)