struct Solution;

impl Solution {
    pub fn gcd(mut x: i32, mut y: i32) -> i32 {
        while y > 0 {
            (x, y) = (y, x % y);
        }

        x
    }

    pub fn find_gcd(nums: Vec<i32>) -> i32 {
        let mut min = i32::MAX;
        let mut max = 0;

        for num in nums {
            min = num.min(min);
            max = num.max(max);
        }

        Solution::gcd(min, max)
    }
}

pub fn main() {
    assert_eq!(Solution::find_gcd(vec![2, 5, 6, 9, 10]), 2);
    assert_eq!(Solution::find_gcd(vec![7, 5, 6, 8, 3]), 1);
    assert_eq!(Solution::find_gcd(vec![3, 3]), 3);
    println!("ok");
}
