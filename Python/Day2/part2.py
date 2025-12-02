from part1 import parse
import math



def main():
    ids = parse()
    result = 0

    for id_range in ids:
        for id_num in id_range:
            if id_num[0] == 0:
                print("Leading Zero")
                result += int(id_num)
            else:
                prev_id_num = ""
                for i in range(1, math.floor(len(id_num) / 2 + 1)):
                    
                    pattern = id_num[0:i]
                    parts = [id_num[j:j + i] for j in range(0, len(id_num), i)]
                                
                    if all(part == pattern for part in parts):
                        if prev_id_num != id_num:
                            print(f"id_num: {id_num}, pattern: {pattern}, parts: {parts}")
                            result += int(id_num)
                            prev_id_num = id_num
                        
    print(result)



if __name__ == "__main__":
    main()