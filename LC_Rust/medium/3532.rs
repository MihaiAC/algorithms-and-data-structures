struct Solution;

impl Solution {
    pub fn find(node: usize, root: &mut Vec<usize>) -> usize {
        if node == root[node] {
            return node;
        }

        root[node] = Self::find(root[node], root);
        root[node]
    }

    pub fn union(node_u: usize, node_v: usize, root: &mut Vec<usize>, size: &mut [usize]) {
        let mut node_u = Self::find(node_u, root);
        let mut node_v = Self::find(node_v, root);

        if node_u == node_v {
            return;
        }

        if size[node_u] > size[node_v] {
            (node_u, node_v) = (node_v, node_u);
        }

        root[node_u] = node_v;
        size[node_v] += size[node_u];
    }

    #[allow(clippy::needless_pass_by_value)]
    #[allow(clippy::cast_sign_loss)]
    pub fn path_existence_queries(
        n: i32,
        nums: Vec<i32>,
        max_diff: i32,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let n = n as usize;

        let mut root: Vec<usize> = (0..n).collect();
        let mut size: Vec<usize> = vec![1; n];

        for idx in 0..(n - 1) {
            if nums[idx + 1] - nums[idx] <= max_diff {
                Solution::union(idx, idx + 1, &mut root, &mut size);
            }
        }

        let mut ans: Vec<bool> = vec![];
        for query in queries {
            ans.push(
                Solution::find(query[0] as usize, &mut root)
                    == Solution::find(query[1] as usize, &mut root),
            );
        }

        ans
    }
}

pub fn main() {
    assert_eq!(
        Solution::path_existence_queries(2, vec![1, 3], 1, vec![vec![0, 0], vec![0, 1]]),
        vec![true, false]
    );

    assert_eq!(
        Solution::path_existence_queries(
            4,
            vec![2, 5, 6, 8],
            2,
            vec![vec![0, 1], vec![0, 2], vec![1, 3], vec![2, 3]]
        ),
        vec![false, false, true, true]
    );

    println!("ok");
}
