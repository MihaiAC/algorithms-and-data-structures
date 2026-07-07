struct Solution;

impl Solution {
    pub fn sum_and_multiply(n: i32) -> i64 {
        let mut n = n;
        let mut sum = 0;
        let mut new_num = 0;
        let mut mult = 1;

        while n > 0 {
            let digit = n % 10;
            if digit > 0 {
                sum += digit;
                new_num += mult * digit;
                mult *= 10;
            }
            n /= 10;
        }

        i64::from(new_num) * i64::from(sum)
    }
}

pub fn main() {
    assert_eq!(Solution::sum_and_multiply(10_203_004), 12340);
    assert_eq!(Solution::sum_and_multiply(1_000), 1);
    println!("ok");
}
