


def parse() -> list:

    with open("./input.txt") as file:
        content = file.read().strip()
        split_content = content.split(",")
        ranges = []

        for item in split_content:
            split_item = item.split("-")
            ranges.append([int(split_item[0]), int(split_item[1])])

        ids_int = []
        for r in ranges:
            ids_int.append(list(range(r[0], r[1] + 1)))
        
    return [[str(num) for num in id_range] for id_range in ids_int]
    


def main():
    ids = parse()
    result = 0

    for id_range in ids:
        for id_num in id_range:
            if id_num[0] == 0:
                print("Leading Zero")
                result += int(id_num)
            else:
                first, second = id_num[:len(id_num) // 2], id_num[len(id_num) // 2:]
                if first == second:
                    result += int(id_num)

    print(result)



if __name__ == "__main__":
    main()