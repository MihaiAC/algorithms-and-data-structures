use std::sync::OnceLock;

static WINS_FROM_HERE: OnceLock<Box<[bool]>> = OnceLock::new();

fn get_wins() -> &'static [bool] {
    WINS_FROM_HERE.get_or_init(|| {
        let mut arr = vec![false; 100_489].into_boxed_slice();

        for root in 1usize..317 {
            for num in root.pow(2)..(root + 1).pow(2) {
                let mut curr = false;
                for sub in 1..=root {
                    if !arr[num - sub.pow(2)] {
                        curr = true;
                        break;
                    }
                }
                arr[num] = curr;
            }
        }
        arr
    })
}

struct Solution;

impl Solution {
    #[allow(clippy::cast_sign_loss)]
    pub fn winner_square_game(n: i32) -> bool {
        get_wins()[n as usize]
    }
}

pub fn main() {
    assert!(Solution::winner_square_game(1));
    assert!(!Solution::winner_square_game(2));
    assert!(Solution::winner_square_game(4));
    assert!(!Solution::winner_square_game(7));
    println!("ok");
}
