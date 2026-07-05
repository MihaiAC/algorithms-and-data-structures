struct Solution;

const MODN: i64 = 10_i64.pow(9) + 7;

impl Solution {
    #[allow(clippy::cast_possible_truncation)]
    pub fn paths_with_max_score(board: Vec<String>) -> Vec<i32> {
        let n = board.len();
        let board: Vec<Vec<u8>> = board.into_iter().map(String::into_bytes).collect();
        let mut score = vec![vec![-1; n]; n];
        let mut count: Vec<Vec<i64>> = vec![vec![0; n]; n];

        score[n - 1][n - 1] = 0;
        count[n - 1][n - 1] = 1;

        for ii in (0..n).rev() {
            for jj in (0..n).rev() {
                if board[ii][jj] == b'X' || (ii == n - 1 && jj == n - 1) {
                    continue;
                }

                Self::update((ii, jj), (ii + 1, jj), n, &mut score, &mut count);
                Self::update((ii, jj), (ii, jj + 1), n, &mut score, &mut count);
                Self::update((ii, jj), (ii + 1, jj + 1), n, &mut score, &mut count);

                if score[ii][jj] != -1 {
                    score[ii][jj] += if board[ii][jj] == b'E' {
                        0
                    } else {
                        i32::from(board[ii][jj] - b'0')
                    };
                }
            }
        }

        if score[0][0] != -1 {
            return vec![score[0][0], (count[0][0] % MODN) as i32];
        }

        vec![0, 0]
    }

    pub fn update(
        (x, y): (usize, usize),
        (prev_x, prev_y): (usize, usize),
        n: usize,
        score: &mut [Vec<i32>],
        count: &mut [Vec<i64>],
    ) {
        if prev_x >= n || prev_y >= n || score[prev_x][prev_y] == -1 {
            return;
        }

        if score[prev_x][prev_y] > score[x][y] {
            score[x][y] = score[prev_x][prev_y];
            count[x][y] = count[prev_x][prev_y];
        } else if score[prev_x][prev_y] == score[x][y] {
            count[x][y] = (count[prev_x][prev_y] + count[x][y]) % MODN;
        }
    }
}

pub fn main() {
    assert_eq!(
        Solution::paths_with_max_score(vec![
            "E23".to_string(),
            "2X2".to_string(),
            "12S".to_string()
        ]),
        vec![7, 1]
    );

    assert_eq!(
        Solution::paths_with_max_score(vec![
            "E12".to_string(),
            "1X1".to_string(),
            "21S".to_string()
        ]),
        vec![4, 2]
    );

    assert_eq!(
        Solution::paths_with_max_score(vec![
            "E11".to_string(),
            "XXX".to_string(),
            "11S".to_string()
        ]),
        vec![0, 0]
    );

    println!("ok");
}
