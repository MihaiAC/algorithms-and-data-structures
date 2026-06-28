struct Solution;

#[allow(clippy::needless_pass_by_value)]
impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(arr: Vec<i32>) -> i32 {
        let mut arr_sorted = arr.clone();
        arr_sorted.sort_unstable();

        let mut reached = 1;

        for elem in &arr_sorted[1..] {
            if *elem > reached {
                reached += 1;
            }
        }

        reached
    }
}

pub fn main() {
    assert_eq!(
        Solution::maximum_element_after_decrementing_and_rearranging(vec![2, 2, 1, 2, 1]),
        2
    );
    assert_eq!(
        Solution::maximum_element_after_decrementing_and_rearranging(vec![100, 1, 1000]),
        3
    );
    assert_eq!(
        Solution::maximum_element_after_decrementing_and_rearranging(vec![1, 2, 3, 4, 5]),
        5
    );
    println!("ok");
}
