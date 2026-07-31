struct Solution;

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    pub fn minimum_pushes(word: String) -> i32 {
        let mut counter = [0; 26];
        for byte in word.bytes() {
            counter[(byte - 97) as usize] += 1;
        }

        let mut freqs: Vec<i32> = counter.into_iter().filter(|&freq| freq > 0).collect();
        freqs.sort_unstable_by(|a, b| b.cmp(a));

        freqs
            .iter()
            .enumerate()
            .map(|(idx, &freq)| freq * (i32::try_from(idx).unwrap() / 8 + 1))
            .sum()
    }
}

pub fn main() {
    assert_eq!(Solution::minimum_pushes("abcde".to_string()), 5);
    assert_eq!(Solution::minimum_pushes("xyzxyzxyzxyz".to_string()), 12);
    assert_eq!(
        Solution::minimum_pushes("aabbccddeeffgghhiiiiii".to_string()),
        24
    );
    println!("ok");
}
