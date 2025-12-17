


def parse() -> list:
    fresh_id_ranges = []

    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            if line == "":
                break
            split_line = line.split("-")
            fresh_id_ranges.append(list(map(int, split_line)))

    return fresh_id_ranges



def main():
    fresh_id_ranges = parse()
    final_ranges = []

    for i in range(len(fresh_id_ranges)):
        if fresh_id_ranges[i] == None:
            continue

        for cmpr_range in fresh_id_ranges:
            if fresh_id_ranges[i] == None or cmpr_range == None:
                continue
            if (fresh_id_ranges[i][0] < cmpr_range[0] and fresh_id_ranges[i][1] > cmpr_range[1]) or fresh_id_ranges[i][0] - 1 == cmpr_range[1]:
                fresh_id_ranges[i] = [cmpr_range[0], fresh_id_ranges[1]]
            elif fresh_id_ranges[i][1] + 1 == cmpr_range[0]:
                fresh_id_ranges[i] = [fresh_id_ranges[i], cmpr_range[1]]
            else:
                final_ranges.append(fresh_id_ranges[i])
                fresh_id_ranges[i] = None

    print(final_ranges)



if __name__ == "__main__":
    main()