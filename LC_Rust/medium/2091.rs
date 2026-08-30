struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let n = nums.len();

        let mut min = i32::MAX;
        let mut min_idx = 0;

        let mut max = i32::MIN;
        let mut max_idx = 0;

        for (idx, num) in nums.iter().enumerate() {
            if *num > max {
                max = nums[idx];
                max_idx = idx;
            }

            if *num < min {
                min = nums[idx];
                min_idx = idx;
            }
        }

        let left_idx = min_idx.min(max_idx);
        let right_idx = min_idx.max(max_idx);

        (right_idx + 1)
            .min(n - left_idx)
            .min(n - right_idx + left_idx + 1)
            .try_into()
            .unwrap()
    }
}

pub fn main() {
    assert_eq!(
        Solution::minimum_deletions(vec![2, 10, 7, 5, 4, 1, 8, 6]),
        5
    );
    assert_eq!(
        Solution::minimum_deletions(vec![0, -4, 19, 1, 8, -2, -3, 5]),
        3
    );
    assert_eq!(Solution::minimum_deletions(vec![101]), 1);
    println!("ok");
}
