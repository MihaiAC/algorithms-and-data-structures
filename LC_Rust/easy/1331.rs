use std::cmp::Ordering;
use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn find_idx(num: i32, sorted_arr: &[i32]) -> i32 {
        let mut left = 0;
        let mut right = sorted_arr.len() - 1;
        let mut middle;

        while left < right {
            middle = left.midpoint(right);
            match num.cmp(&sorted_arr[middle]) {
                Ordering::Equal => return i32::try_from(middle).unwrap(),
                Ordering::Greater => left = middle + 1,
                Ordering::Less => right = middle,
            }
        }

        i32::try_from(left).unwrap()
    }

    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut sorted_arr: Vec<i32> = (arr.iter().copied().collect::<HashSet<i32>>())
            .into_iter()
            .collect();
        sorted_arr.sort_unstable();

        let mut ans = vec![];

        for num in arr {
            ans.push(Solution::find_idx(num, &sorted_arr) + 1);
        }

        ans
    }
}

pub fn main() {
    assert_eq!(
        Solution::array_rank_transform(vec![40, 10, 20, 30]),
        vec![4, 1, 2, 3]
    );

    assert_eq!(
        Solution::array_rank_transform(vec![100, 100, 100]),
        vec![1, 1, 1]
    );

    assert_eq!(
        Solution::array_rank_transform(vec![37, 12, 28, 9, 100, 56, 80, 5, 12]),
        vec![5, 3, 4, 2, 8, 6, 7, 1, 3]
    );

    println!("ok");
}
