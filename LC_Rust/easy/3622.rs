struct Solution;

impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let mut n_copy = n.to_owned();
        let mut prod = 1;
        let mut sum = 0;

        while n_copy > 0 {
            let digit = n_copy % 10;
            prod *= digit;
            sum += digit;

            n_copy /= 10;
        }

        n % (prod + sum) == 0
    }
}

pub fn main() {
    assert!(Solution::check_divisibility(99));
    assert!(!Solution::check_divisibility(23));
    println!("ok");
}
