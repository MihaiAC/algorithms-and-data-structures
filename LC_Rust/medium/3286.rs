use std::collections::BinaryHeap;

struct Solution;

const DELTAS: [(i32, i32); 4] = [(0, 1), (0, -1), (-1, 0), (1, 0)];

impl Solution {
    #[allow(clippy::needless_pass_by_value)]
    #[allow(clippy::cast_possible_truncation)]
    #[allow(clippy::cast_possible_wrap)]
    #[allow(clippy::cast_sign_loss)]
    pub fn find_safe_walk(grid: Vec<Vec<i32>>, health: i32) -> bool {
        if health == 1 && grid[0][0] == 1 {
            return false;
        }

        let m: usize = grid.len();
        let n: usize = grid[0].len();

        let in_bounds = |x: usize, y: usize, dx: i32, dy: i32| {
            (x as i32) + dx >= 0
                && (x as i32) + dx < (m as i32)
                && (y as i32) + dy >= 0
                && (y as i32) + dy < (n as i32)
        };

        let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
        let mut heap: BinaryHeap<(i32, usize, usize)> = BinaryHeap::new();

        visited[0][0] = true;
        heap.push((health - grid[0][0], 0, 0));
        while !heap.is_empty() {
            let (curr_health, x, y) = heap.pop().unwrap();
            for (dx, dy) in DELTAS {
                if !in_bounds(x, y, dx, dy) {
                    continue;
                }

                let nx = (x as i32 + dx) as usize;
                let ny = (y as i32 + dy) as usize;

                if visited[nx][ny] {
                    continue;
                }

                if (grid[nx][ny] == 1 && curr_health > 1) || grid[nx][ny] == 0 {
                    if nx == m - 1 && ny == n - 1 {
                        return true;
                    }

                    visited[nx][ny] = true;
                    heap.push((curr_health - grid[nx][ny], nx, ny));
                }
            }
        }

        false
    }
}

pub fn main() {
    assert!(Solution::find_safe_walk(
        vec![
            vec![0, 1, 0, 0, 0],
            vec![0, 1, 0, 1, 0],
            vec![0, 0, 0, 1, 0]
        ],
        1
    ));

    assert!(!Solution::find_safe_walk(
        vec![
            vec![0, 1, 1, 0, 0, 0],
            vec![1, 0, 1, 0, 0, 0],
            vec![0, 1, 1, 1, 0, 1],
            vec![0, 0, 1, 0, 1, 0]
        ],
        3
    ));

    assert!(Solution::find_safe_walk(
        vec![vec![1, 1, 1], vec![1, 0, 1], vec![1, 1, 1]],
        5
    ));
    println!("ok");
}
