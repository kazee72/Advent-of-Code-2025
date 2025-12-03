


def parse() -> list:
    banks = []

    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            bank = []
            for digit in line:
                bank.append(digit) 

            banks.append(bank)

    return banks



def main():
    banks = parse()
    result = 0

    for bank in banks:
        largest = 0
        for i in range(0, len(bank) - 1):
            for j in range(i + 1, len(bank)):
                joltage = bank[i] + bank[j]
                if int(joltage) > largest:
                    largest = int(joltage)

        result += largest

    print(result)



if __name__ == "__main__":
    main()