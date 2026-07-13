struct Solution;

const DIGITS: &str = "123456789";

impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut ans = vec![];
        let mut n_digits = (low.ilog10() + 1) as usize;

        loop {
            if n_digits > 9 {
                return ans;
            }

            for idx in 0..(10 - n_digits) {
                let curr_slice = DIGITS[idx..(idx + n_digits)].parse::<i32>().unwrap();

                if curr_slice < low {
                    continue;
                }

                if curr_slice <= high {
                    ans.push(curr_slice);
                } else {
                    return ans;
                }
            }

            n_digits += 1;
        }
    }
}

pub fn main() {
    assert_eq!(Solution::sequential_digits(100, 300), vec![123, 234]);
    assert_eq!(
        Solution::sequential_digits(1000, 13000),
        vec![1234, 2345, 3456, 4567, 5678, 6789, 12345]
    );
    println!("ok");
}
