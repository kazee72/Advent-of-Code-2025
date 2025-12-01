from part1 import parse



def main():
    rotations = parse()
    current_pos = 50
    
    wraps = 0

    for dir, amount in rotations:

        if dir == "L":
            if amount > current_pos:
                wraps += amount // 100
                if amount % 100 > current_pos and current_pos != 0:
                    wraps += 1
            current_pos -= amount

        else:
            if amount + current_pos > 99:
                wraps += amount // 100
                if amount % 100 + current_pos > 100:
                    wraps += 1
            current_pos += amount
    
        current_pos = current_pos % 100

        if current_pos == 0:
            wraps += 1

    print(wraps)



if __name__ == "__main__":
    main()