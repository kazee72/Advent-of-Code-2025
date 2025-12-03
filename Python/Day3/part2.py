from part1 import parse



def get_largest(bank: list, start_indx: int, num_left: int, result: str):
    if num_left < 0:
        return result
    
    largest = 0
    largest_indx = 0
    for i in range(start_indx, len(bank) - num_left):
        if int(bank[i]) > largest:
            largest = int(bank[i])
            largest_indx = i
    result += str(largest)

    return get_largest(bank, largest_indx + 1, num_left - 1, result)

    

def main():
    banks = parse()
    result = 0

    for bank in banks:
        largest = get_largest(bank, 0, 11, "")
        result += int(largest)

    print(result)

    

if __name__ == "__main__":
    main()