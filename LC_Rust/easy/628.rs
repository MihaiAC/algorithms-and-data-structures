struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    pub fn maximum_product(nums: Vec<i32>) -> i32 {
        if nums.len() == 3 {
            return nums[0] * nums[1] * nums[2];
        }

        let mut largest = -1001;
        let mut largest_ii = -1001;
        let mut largest_iii = -1001;

        let mut smallest_i = 1001;
        let mut smallest_ii = 1001;

        for num in nums {
            if num > largest {
                largest_iii = largest_ii;
                largest_ii = largest;
                largest = num;
            } else if num > largest_ii {
                largest_iii = largest_ii;
                largest_ii = num;
            } else if num > largest_iii {
                largest_iii = num;
            }

            if num < smallest_i {
                smallest_ii = smallest_i;
                smallest_i = num;
            } else if num < smallest_ii {
                smallest_ii = num;
            }
        }

        (smallest_i * smallest_ii * largest).max(largest * largest_ii * largest_iii)
    }
}

pub fn main() {
    assert_eq!(Solution::maximum_product(vec![1, 2, 3]), 6);
    assert_eq!(Solution::maximum_product(vec![1, 2, 3, 4]), 24);
    assert_eq!(Solution::maximum_product(vec![-1, -2, -3]), -6);
    println!("ok");
}
