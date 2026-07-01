use std::collections::{BinaryHeap, VecDeque};

const DELTAS: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

struct Solution;

impl Solution {
    #[allow(clippy::cast_possible_truncation)]
    #[allow(clippy::cast_possible_wrap)]
    #[allow(clippy::cast_sign_loss)]
    #[allow(clippy::needless_pass_by_value)]
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();

        if grid[0][0] == 1 || grid[n - 1][n - 1] == 1 {
            return 0;
        }

        let in_bounds = |x: i32, y: i32| x >= 0 && y >= 0 && x < n as i32 && y < n as i32;

        let mut dist: Vec<Vec<i32>> = vec![vec![-1; n]; n];
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();

        for row in 0..n {
            for col in 0..n {
                if grid[row][col] == 1 {
                    dist[row][col] = 0;
                    queue.push_back((row, col));
                }
            }
        }

        let mut safeness = 0i32;
        while !queue.is_empty() {
            safeness += 1;

            for _ in 0..queue.len() {
                let (x, y) = queue.pop_front().unwrap();

                for (dx, dy) in DELTAS {
                    let nx = x as i32 + dx;
                    let ny = y as i32 + dy;

                    if in_bounds(nx, ny) {
                        let (nx, ny) = (nx as usize, ny as usize);

                        if dist[nx][ny] == -1 {
                            dist[nx][ny] = safeness;
                            queue.push_back((nx, ny));
                        }
                    }
                }
            }
        }

        let mut pq: BinaryHeap<(i32, usize, usize)> = BinaryHeap::new();
        pq.push((dist[0][0], 0, 0));
        dist[0][0] = -1;

        while !pq.is_empty() {
            let (curr_safeness, x, y) = pq.pop().unwrap();

            for (dx, dy) in DELTAS {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;

                if nx >= 0 && ny >= 0 && nx < (n as i32) && ny < (n as i32) {
                    let (nx, ny) = (nx as usize, ny as usize);

                    if dist[nx][ny] > 0 {
                        let new_safeness = curr_safeness.min(dist[nx][ny]);

                        if nx == n - 1 && ny == n - 1 {
                            return new_safeness;
                        }

                        pq.push((new_safeness, nx, ny));
                        dist[nx][ny] = -1;
                    }
                }
            }
        }

        0
    }
}

pub fn main() {
    assert_eq!(
        Solution::maximum_safeness_factor(vec![vec![1, 0, 0], vec![0, 0, 0], vec![0, 0, 1]]),
        0
    );

    assert_eq!(
        Solution::maximum_safeness_factor(vec![vec![0, 0, 1], vec![0, 0, 0], vec![0, 0, 0]]),
        2
    );

    assert_eq!(
        Solution::maximum_safeness_factor(vec![
            vec![0, 0, 0, 1],
            vec![0, 0, 0, 0],
            vec![0, 0, 0, 0],
            vec![1, 0, 0, 0]
        ]),
        2
    );

    println!("ok");
}
