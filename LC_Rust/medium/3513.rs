struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    #[allow(clippy::cast_possible_truncation)]
    #[allow(clippy::cast_possible_wrap)]
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 2 {
            return n as i32;
        }
        (n + 1).next_power_of_two() as i32
    }
}

pub fn main() {
    assert_eq!(Solution::unique_xor_triplets(vec![1, 2]), 2);
    assert_eq!(Solution::unique_xor_triplets(vec![3, 1, 2]), 4);
    println!("ok");
}
