use std::collections::HashMap;

struct Solution;

impl Solution {
    #[allow(clippy::cast_possible_wrap)]
    #[allow(clippy::cast_possible_truncation)]
    #[allow(clippy::needless_pass_by_value)]
    pub fn number_of_substrings(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut left_idx = 0;
        let n = s.len();
        let mut curr_letters: HashMap<char, i32> = HashMap::new();

        let mut ans = 0;

        for (curr_idx, curr_char) in chars.iter().enumerate() {
            *curr_letters.entry(*curr_char).or_insert(0) += 1;
            while curr_letters.len() == 3 && left_idx < curr_idx {
                ans += n - curr_idx;
                *curr_letters.entry(chars[left_idx]).or_insert(0) -= 1;

                if curr_letters.contains_key(&chars[left_idx])
                    && curr_letters[&chars[left_idx]] == 0
                {
                    curr_letters.remove(&chars[left_idx]);
                }

                left_idx += 1;
            }
        }
        ans as i32
    }
}

pub fn main() {
    assert_eq!(Solution::number_of_substrings("abcabc".to_string()), 10);
    assert_eq!(Solution::number_of_substrings("aaacb".to_string()), 3);
    assert_eq!(Solution::number_of_substrings("abc".to_string()), 1);
}
