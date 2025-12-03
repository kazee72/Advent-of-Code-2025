use std::fs;



fn parse() -> Vec<(String, i32)> {
    let mut rotations: Vec<(String, i32)> = Vec::new();
    let file_contents = fs::read_to_string("./input.txt").expect("Failed to read file.");
    let lines: Vec<String> = file_contents.lines().map(|s| s.to_string()).collect();

    for line in lines {
        let key: &str = &line[0..1];
        let value: &str = &line[1..];
        let value_int: i32 = value.parse().expect("Failed to parse to int.");
        rotations.push((key.to_string(), value_int));
    }

    return rotations;
}



fn main() {
    let rotations: Vec<(String, i32)> = parse();
    let dial: Vec<u32> = (0..100).collect();
    let mut counter: u32 = 0;
    let mut current_pos: i32 = 50;

    for (dir, amount) in rotations {
        if dir == "L" {
            current_pos -= amount;
        } else {
            current_pos += amount;
        }

        current_pos = current_pos.rem_euclid(100);

        if dial[current_pos as usize] == 0 {
            counter += 1;
        }
    }

    println!("{}", counter);

}