struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals.clone();
        intervals.sort_by_key(|x| (x[0], std::cmp::Reverse(x[1])));

        let mut ans = 0;
        let mut right = 0;

        for interval in intervals {
            let curr_right = interval[1];

            if curr_right > right {
                ans += 1;
                right = curr_right;
            }
        }

        ans
    }
}

pub fn main() {
    assert_eq!(
        Solution::remove_covered_intervals(vec![vec![1, 4], vec![3, 6], vec![2, 8]]),
        2
    );

    assert_eq!(
        Solution::remove_covered_intervals(vec![vec![1, 4], vec![2, 3]]),
        1
    );
}
