from part1 import parse
import time



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
    start = time.time()
    banks = parse()
    result = 0

    for bank in banks:
        largest = get_largest(bank, 0, 11, "")
        result += int(largest)

    print(result)
    end = time.time()
    print(end - start)

    

if __name__ == "__main__":
    main()