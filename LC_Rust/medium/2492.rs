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
        dist: i32,
        root: &mut Vec<usize>,
        size: &mut [usize],
        min_dist: &mut [i32],
    ) {
        let mut node_u = Self::find(node_u, root);
        let mut node_v = Self::find(node_v, root);

        if node_u == node_v {
            min_dist[node_u] = min_dist[node_u].min(dist);
            return;
        }

        if size[node_u] > size[node_v] {
            (node_u, node_v) = (node_v, node_u);
        }

        root[node_u] = node_v;
        size[node_v] += size[node_u];
        min_dist[node_v] = min_dist[node_u].min(min_dist[node_v]).min(dist);
    }

    #[allow(clippy::cast_sign_loss)]
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut root: Vec<usize> = (0..=n).collect();
        let mut size: Vec<usize> = vec![1; n + 1];
        let mut min_dist = vec![i32::MAX; n + 1];

        for road in roads {
            let (node_u, node_v, dist) = (road[0] as usize, road[1] as usize, road[2]);
            Self::union(node_u, node_v, dist, &mut root, &mut size, &mut min_dist);
        }

        min_dist[Self::find(1, &mut root)]
    }
}

pub fn main() {
    assert_eq!(
        Solution::min_score(
            4,
            vec![vec![1, 2, 9], vec![2, 3, 6], vec![2, 4, 5], vec![1, 4, 7]]
        ),
        5
    );

    assert_eq!(
        Solution::min_score(4, vec![vec![1, 2, 2], vec![1, 3, 4], vec![3, 4, 7]]),
        2
    );

    println!("ok");
}
