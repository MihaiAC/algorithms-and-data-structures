use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn get_score(
        player: bool,
        idx: usize,
        memo: &mut HashMap<(bool, usize), i32>,
        stone_value: &[i32],
    ) -> i32 {
        if idx >= stone_value.len() {
            return 0;
        }

        if memo.contains_key(&(player, idx)) {
            return *memo.get(&(player, idx)).unwrap();
        }

        let value_at = |offset: usize| stone_value.get(offset).copied().unwrap_or(0);

        let score = if player {
            Solution::get_score(false, idx + 1, memo, stone_value)
                .min(Solution::get_score(false, idx + 2, memo, stone_value))
                .min(Solution::get_score(false, idx + 3, memo, stone_value))
        } else {
            let take_one = value_at(idx) + Solution::get_score(true, idx + 1, memo, stone_value);
            let take_two = value_at(idx)
                + value_at(idx + 1)
                + Solution::get_score(true, idx + 2, memo, stone_value);
            let take_three = value_at(idx)
                + value_at(idx + 1)
                + value_at(idx + 2)
                + Solution::get_score(true, idx + 3, memo, stone_value);

            take_one.max(take_two).max(take_three)
        };

        memo.insert((player, idx), score);

        score
    }

    #[allow(clippy::needless_pass_by_value)]
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        let mut memo: HashMap<(bool, usize), i32> = HashMap::new();

        let total: i32 = stone_value.iter().sum();
        let alice = Solution::get_score(false, 0, &mut memo, &stone_value);
        let bob = total - alice;

        match alice.cmp(&bob) {
            std::cmp::Ordering::Greater => "Alice".to_string(),
            std::cmp::Ordering::Equal => "Tie".to_string(),
            std::cmp::Ordering::Less => "Bob".to_string(),
        }
    }
}

pub fn main() {
    assert_eq!(Solution::stone_game_iii(vec![1, 2, 3, 7]), "Bob");
    assert_eq!(Solution::stone_game_iii(vec![1, 2, 3, -9]), "Alice");
    assert_eq!(Solution::stone_game_iii(vec![1, 2, 3, 6]), "Tie");
    println!("ok");
}
