class Solution:
    def countTriples(self, n: int) -> int:
        squares_arr = []
        squares_set = set()

        for num in range(1, n + 1):
            num_sq = num**2
            squares_set.add(num_sq)
            squares_arr.append(num_sq)

        ans = 0
        for a_idx in range(len(squares_arr) - 1):
            a = squares_arr[a_idx]
            for c_idx in range(a_idx + 1, len(squares_arr)):
                c = squares_arr[c_idx]
                if (c - a) in squares_set:
                    ans += 1

        return ans
