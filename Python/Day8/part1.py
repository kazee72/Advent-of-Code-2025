import math



def parse() -> list:
    junction_boxes = []

    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            boxes = line.split(",")
            junction_boxes.append(list(map(int, boxes)))

    return junction_boxes



def main():
    junction_boxes = parse()
    circuits = []

    for box1 in junction_boxes:
        closest_dist = float('inf')
        for box2 in junction_boxes:
            if math.dist(box1, box2) == 0:
                continue
            if math.dist(box1, box2) < closest_dist:
                closest_dist = math.dist(box1, box2)
                closest_box = box2
        
        circuits.append([box1, closest_box])

    
    for circuit in circuits:
        print(f"boxes: {circuit}")

        



    
    
    



if __name__ == "__main__":
    main()