struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        let mut ans = 0;
        for pattern in patterns {
            if word.contains(pattern.as_str()) {
                ans += 1;
            }
        }
        ans
    }
}

pub fn convert_to_string(input: Vec<&str>) -> Vec<String> {
    input.into_iter().map(String::from).collect()
}

pub fn main() {
    assert_eq!(
        Solution::num_of_strings(
            convert_to_string(vec!["a", "abc", "bc", "d"]),
            "abc".to_string()
        ),
        3
    );
    assert_eq!(
        Solution::num_of_strings(
            convert_to_string(vec!["a", "b", "c"]),
            "aaaaabbbbb".to_string()
        ),
        2
    );
    assert_eq!(
        Solution::num_of_strings(convert_to_string(vec!["a", "a", "a"]), "ab".to_string()),
        3
    );
}
