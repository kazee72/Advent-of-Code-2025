


def parse():
    fresh_id_ranges = []
    available_ids = []
    is_available_id = False
    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            if line == "":
                is_available_id = True
                continue

            if is_available_id:
                available_ids.append(int(line))
            else:
                ids = line.split("-")
                fresh_id_ranges.append((int(ids[0]), int(ids[1])))

    return fresh_id_ranges, available_ids



def main():
    fresh_ids, available_ids = parse()
    result = 0

    for id in available_ids:
        for id_range in fresh_ids:
            if id > id_range[0] and id < id_range[1]:
                result += 1
                break
    
    print(result)





if __name__ == "__main__":
    main()