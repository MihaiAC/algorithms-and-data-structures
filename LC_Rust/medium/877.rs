struct Solution;

impl Solution {
    pub fn stone_game(_piles: Vec<i32>) -> bool {
        true
    }
}

pub fn main() {
    assert!(Solution::stone_game(vec![3, 7, 2, 3]));
    println!("ok");
}
