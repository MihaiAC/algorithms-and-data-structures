fn gospers_hack(n: u32) -> u32 {
    let c = n & n.wrapping_neg();
    let r = n + c;
    (((r ^ n) >> 2) / c) | r
}

fn main() {
    for mut num in [1, 3, 7, 15] {
        print!("{num}: ");
        for _ in 0..10 {
            num = gospers_hack(num);
            print!("{num} ");
        }
        println!();
    }
}
