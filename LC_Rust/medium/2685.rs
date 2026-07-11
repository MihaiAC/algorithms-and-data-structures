struct Solution;

impl Solution {
    pub fn find(node: usize, root: &mut Vec<usize>) -> usize {
        if node == root[node] {
            return node;
        }

        root[node] = Self::find(root[node], root);
        root[node]
    }

    pub fn union(
        node_u: usize,
        node_v: usize,
        root: &mut Vec<usize>,
        size: &mut [usize],
        n_edges: &mut [usize],
    ) {
        let mut node_u = Self::find(node_u, root);
        let mut node_v = Self::find(node_v, root);

        if node_u != node_v {
            if size[node_u] > size[node_v] {
                (node_u, node_v) = (node_v, node_u);
            }

            root[node_u] = node_v;
            size[node_v] += size[node_u];
            n_edges[node_v] += n_edges[node_u];
        }

        n_edges[node_v] += 1;
    }

    #[allow(clippy::needless_pass_by_value)]
    #[allow(clippy::cast_sign_loss)]
    #[allow(clippy::cast_possible_truncation)]
    #[allow(clippy::cast_possible_wrap)]
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;

        let mut root: Vec<usize> = (0..n).collect();
        let mut size: Vec<usize> = vec![1; n];
        let mut n_edges: Vec<usize> = vec![0; n];

        for edge in edges {
            Solution::union(
                edge[0] as usize,
                edge[1] as usize,
                &mut root,
                &mut size,
                &mut n_edges,
            );
        }

        let mut ans = 0;
        for node in 0..n {
            if node == Solution::find(node, &mut root)
                && size[node] * (size[node] - 1) / 2 == n_edges[node]
            {
                ans += 1;
            }
        }

        ans
    }
}

pub fn main() {
    assert_eq!(
        Solution::count_complete_components(
            6,
            vec![vec![0, 1], vec![0, 2], vec![1, 2], vec![3, 4]]
        ),
        3
    );

    assert_eq!(
        Solution::count_complete_components(
            6,
            vec![vec![0, 1], vec![0, 2], vec![1, 2], vec![3, 4], vec![3, 5]]
        ),
        1
    );

    assert_eq!(Solution::count_complete_components(1, vec![]), 1);

    assert_eq!(
        Solution::count_complete_components(4, vec![vec![0, 1], vec![2, 3]]),
        2
    );

    println!("ok");
}
