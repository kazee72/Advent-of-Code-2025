


def parse() -> list:
    rolls = []

    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            line_array = []
            for char in line:
                line_array.append(char)
            rolls.append(line_array)

    return rolls

def main():
    rolls = parse()
    result = 0
    for roll in rolls:
        print(roll)

    for i in range(0, len(rolls)):
        for j in range(0, len(rolls[0])):
            neighbours = 0
            if rolls[i][j] != '@':
                continue

            for offsetr in [-1, 0, 1]:
                for offsetc in [-1, 0, 1]:
                    if offsetr == 0 and offsetc == 0:
                        continue

                    neighbour_row = i + offsetr
                    neighbour_col = j + offsetc

                    if neighbour_row < 0 or neighbour_row >= len(rolls):
                        continue
                    if neighbour_col < 0 or neighbour_col >= len(rolls[0]):
                        continue

                    try:
                        neighbours += 1 if rolls[neighbour_row][neighbour_col] == '@' else 0
                    except IndexError:
                        pass        

            if neighbours < 4:
                result += 1


    print(result)



if __name__ == "__main__":
    main()