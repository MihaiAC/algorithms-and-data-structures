use std::collections::HashMap;

struct Solution;

const MIN_SUM: i32 = 1_000_000;

impl Solution {
    pub fn calc_piles(
        memo: &mut HashMap<(bool, usize, usize), i32>,
        piles: &Vec<i32>,
        player: bool,
        idx: usize,
        m: usize,
    ) -> i32 {
        if memo.contains_key(&(player, idx, m)) {
            return *memo.get(&(player, idx, m)).unwrap();
        }

        if idx + 2 * m >= piles.len() {
            if player {
                return 0;
            }
            return piles[idx..].iter().sum();
        }

        let mut points = 0;
        if player {
            points = MIN_SUM;
            for dx in 0..(2 * m) {
                points = points.min(Solution::calc_piles(
                    memo,
                    piles,
                    false,
                    idx + dx + 1,
                    piles.len().min(m.max(dx + 1)),
                ));
            }
        } else {
            let mut cumsum = 0;

            for dx in 0..(2 * m) {
                cumsum += piles[idx + dx];
                points = points.max(
                    cumsum
                        + Solution::calc_piles(
                            memo,
                            piles,
                            true,
                            idx + dx + 1,
                            piles.len().min(m.max(dx + 1)),
                        ),
                );
            }
        }

        memo.insert((player, idx, m), points);
        points
    }

    #[allow(clippy::needless_pass_by_value)]
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        let mut memo: HashMap<(bool, usize, usize), i32> = HashMap::new();
        Solution::calc_piles(&mut memo, &piles, false, 0, 1)
    }
}

pub fn main() {
    assert_eq!(Solution::stone_game_ii(vec![2, 7, 9, 4, 4]), 10);
    assert_eq!(Solution::stone_game_ii(vec![1, 2, 3, 4, 5, 100]), 104);
    println!("ok");
}
