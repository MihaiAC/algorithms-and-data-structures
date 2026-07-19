use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    pub fn smallest_subsequence(s: String) -> String {
        let s = s.as_bytes();

        let mut selected: HashSet<u8> = HashSet::new();
        let mut last_idx: HashMap<u8, usize> = HashMap::new();
        let mut stack: Vec<u8> = vec![];

        for (idx, letter) in s.iter().enumerate() {
            last_idx.insert(*letter, idx);
        }

        for (idx, letter) in s.iter().enumerate() {
            if selected.contains(letter) {
                continue;
            }

            while !stack.is_empty()
                && letter < stack.last().unwrap()
                && idx < *last_idx.get(stack.last().unwrap()).unwrap()
            {
                selected.remove(&stack.pop().unwrap());
            }

            selected.insert(*letter);
            stack.push(*letter);
        }

        String::from_utf8(stack).unwrap()
    }
}

pub fn main() {
    assert_eq!(
        Solution::smallest_subsequence("bcabc".to_string()),
        "abc".to_string()
    );

    assert_eq!(
        Solution::smallest_subsequence("cbacdcbc".to_string()),
        "acdb".to_string()
    );

    println!("ok");
}
