


def parse() -> list:
    rotations = []

    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            key = line[0]
            value = int(line[1:])
            rotations.append((key, value))

    return rotations


def main():
    rotations = parse()
    dial = list(range(0, 100))
    counter = 0

    current_pos = 50

    for dir, amount in rotations:
        if dir == "L":
            current_pos -= amount
        else:
            current_pos += amount
            
        current_pos = current_pos % 100

        if dial[current_pos] == 0:
            counter += 1
        
    
    print(f"Password: {counter}")
        

            



    

    



if __name__ == "__main__":
    main()