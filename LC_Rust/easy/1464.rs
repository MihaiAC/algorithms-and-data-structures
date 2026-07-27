struct Solution;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max1 = 0;
        let mut max2 = 0;

        for num in nums {
            if num > max1 {
                max2 = max1;
                max1 = num;
            } else if num > max2 {
                max2 = num;
            }
        }

        (max1 - 1) * (max2 - 1)
    }
}

pub fn main() {
    assert_eq!(Solution::max_product(vec![3, 4, 5, 2]), 12);
    assert_eq!(Solution::max_product(vec![1, 5, 4, 5]), 16);
    assert_eq!(Solution::max_product(vec![3, 7]), 12);
    println!("ok");
}
