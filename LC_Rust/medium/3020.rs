use itertools::Itertools;
use std::cmp::max;
use std::collections::HashMap;

struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        #[allow(clippy::cast_possible_truncation)]
        #[allow(clippy::cast_possible_wrap)]
        let counts: HashMap<&i32, i32> = nums
            .iter()
            .counts()
            .into_iter()
            .map(|(k, v)| (k, v as i32))
            .collect();
        let mut ans: i32 = 1;

        // Handle 1s.
        let mut ones_len: i32 = counts.get(&1).copied().unwrap_or(0);
        if ones_len % 2 == 0 {
            ones_len -= 1;
        }
        ans = max(ans, ones_len);

        // Handle the others.
        for (num, count) in &counts {
            if **num == 1 || *count < 2 {
                continue;
            }

            let mut curr_len = 0;
            let mut curr_num = **num;
            loop {
                if !counts.contains_key(&curr_num) {
                    curr_len -= 1;
                    break;
                } else if counts.get(&curr_num) == Some(&1) {
                    curr_len += 1;
                    break;
                }
                curr_num = curr_num.pow(2);
                curr_len += 2;
            }

            ans = max(ans, curr_len);
        }

        ans
    }
}

pub fn main() {
    assert_eq!(Solution::maximum_length(vec![5, 4, 1, 2, 2]), 3);
    assert_eq!(Solution::maximum_length(vec![1, 3, 2, 4]), 1);
    assert_eq!(Solution::maximum_length(vec![4, 36, 81, 16, 25]), 1);
    println!("ok");
}
