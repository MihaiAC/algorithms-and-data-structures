use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};

struct Solution;

impl Solution {
    #[allow(clippy::cast_sign_loss)]
    #[allow(clippy::cast_possible_truncation)]
    #[allow(clippy::cast_possible_wrap)]
    #[allow(clippy::needless_pass_by_value)]
    pub fn find_max_path_score(edges: Vec<Vec<i32>>, online: Vec<bool>, k: i64) -> i32 {
        let mut sorted_weights: Vec<i32> = vec![];
        let mut neighbors: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();
        let n = online.len() as i32;

        for edge in edges {
            let (u, v, weight) = (edge[0], edge[1], edge[2]);
            if !online[u as usize] || !online[v as usize] {
                continue;
            }

            sorted_weights.push(weight);
            neighbors.entry(u).or_default().push((v, weight));
        }

        sorted_weights.sort_unstable();
        sorted_weights.dedup();

        if sorted_weights.is_empty() || !Solution::dijkstra(&neighbors, k, sorted_weights[0], n) {
            return -1;
        }

        let mut left: usize = 0;
        let mut right: usize = sorted_weights.len() - 1;
        while left < right {
            let mid = usize::midpoint(left + 1, right);
            if Solution::dijkstra(&neighbors, k, sorted_weights[mid], n) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }

        sorted_weights[left]
    }

    #[allow(clippy::cast_possible_wrap)]
    #[allow(clippy::cast_lossless)]
    pub fn dijkstra(
        neighbors: &HashMap<i32, Vec<(i32, i32)>>,
        k: i64,
        min_weight: i32,
        n: i32,
    ) -> bool {
        let mut heap: BinaryHeap<(Reverse<i64>, i32)> = BinaryHeap::new();
        heap.push((Reverse(0), 0));

        while !heap.is_empty() {
            let (Reverse(path_sum), curr_node) = heap.pop().unwrap();

            if curr_node == (n - 1) {
                return true;
            }

            if let Some(adj) = neighbors.get(&curr_node) {
                for (next_node, weight) in adj {
                    if *weight < min_weight {
                        continue;
                    }

                    let next_sum = path_sum + (*weight as i64);
                    if next_sum <= k {
                        heap.push((Reverse(next_sum), *next_node));
                    }
                }
            }
        }

        false
    }
}

pub fn main() {
    assert_eq!(
        Solution::find_max_path_score(
            vec![vec![0, 1, 5], vec![1, 3, 10], vec![0, 2, 3], vec![2, 3, 4]],
            vec![true, true, true, true],
            10
        ),
        3
    );

    assert_eq!(
        Solution::find_max_path_score(
            vec![
                vec![0, 1, 7],
                vec![1, 4, 5],
                vec![0, 2, 6],
                vec![2, 3, 6],
                vec![3, 4, 2],
                vec![2, 4, 6]
            ],
            vec![true, true, true, false, true],
            12
        ),
        6
    );

    println!("ok");
}
