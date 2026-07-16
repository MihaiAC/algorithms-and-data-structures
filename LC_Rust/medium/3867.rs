struct Solution;

impl Solution {
    pub fn gcd(mut first: i32, mut second: i32) -> i32 {
        while second != 0 {
            (first, second) = (second, first % second);
        }
        first
    }

    pub fn gcd_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut curr_max: i32 = 0;
        let mut prefix_gcd = vec![];

        for num in nums {
            curr_max = curr_max.max(num);
            prefix_gcd.push(Solution::gcd(curr_max, num));
        }

        prefix_gcd.sort_unstable();

        let mut ans: i64 = 0;
        for idx in 0..n {
            if idx >= n - 1 - idx {
                break;
            }

            ans += i64::from(Solution::gcd(prefix_gcd[idx], prefix_gcd[n - 1 - idx]));
        }

        ans
    }
}

pub fn main() {
    assert_eq!(Solution::gcd_sum(vec![2, 6, 4]), 2);
    assert_eq!(Solution::gcd_sum(vec![3, 6, 2, 8]), 5);
    println!("ok");
}
