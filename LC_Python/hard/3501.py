from typing import List
from bisect import bisect_left, bisect_right


class SegmentTree:
    def __init__(self, pair_sums: List[int]):
        self.N = len(pair_sums)
        self.max_tree = [0] * (4 * self.N)

        if len(pair_sums) > 0:
            self._build(pair_sums, 1, 0, self.N - 1)

    def _build(self, pair_sums: List[int], node: int, seg_left: int, seg_right: int):
        if seg_left == seg_right:
            self.max_tree[node] = pair_sums[seg_left]
            return

        mid = (seg_left + seg_right) // 2
        self._build(pair_sums, 2 * node, seg_left, mid)
        self._build(pair_sums, 2 * node + 1, mid + 1, seg_right)
        self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])

    def query(self, query_left: int, query_right: int) -> int:
        return self._query(1, 0, self.N - 1, query_left, query_right)

    def _query(
        self,
        node: int,
        seg_left: int,
        seg_right: int,
        query_left: int,
        query_right: int,
    ) -> int:
        if query_left > query_right:
            return 0

        if query_left == seg_left and query_right == seg_right:
            return self.max_tree[node]

        mid = (seg_left + seg_right) // 2

        left_max = self._query(
            2 * node, seg_left, mid, query_left, min(query_right, mid)
        )

        right_max = self._query(
            2 * node + 1, mid + 1, seg_right, max(query_left, mid + 1), query_right
        )

        return max(left_max, right_max)


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        N = len(s)
        ones_count = 0
        blocks = []
        curr_left = -1

        for idx in range(N):
            if s[idx] == "0":
                if curr_left == -1:
                    curr_left = idx
            else:
                ones_count += 1
                if curr_left != -1:
                    blocks.append((idx - curr_left, curr_left, idx - 1))
                    curr_left = -1
        if curr_left != -1:
            blocks.append((N - curr_left, curr_left, N - 1))

        M = len(blocks)
        if M < 2:
            return [ones_count] * len(queries)

        pair_sums = []
        for idx in range(M - 1):
            pair_sums.append(blocks[idx][0] + blocks[idx + 1][0])
        segment_tree = SegmentTree(pair_sums)

        ans = []
        for query_left, query_right in queries:
            left_block_idx = bisect_left(blocks, query_left, key=lambda x: x[2])
            right_block_idx = bisect_right(blocks, query_right, key=lambda x: x[1]) - 1

            if (
                left_block_idx == M
                or right_block_idx < 0
                or left_block_idx >= right_block_idx
            ):
                ans.append(ones_count)
                continue

            left_block_len = (
                blocks[left_block_idx][2]
                - max(blocks[left_block_idx][1], query_left)
                + 1
            )

            right_block_len = (
                min(blocks[right_block_idx][2], query_right)
                - blocks[right_block_idx][1]
                + 1
            )

            if left_block_idx + 1 == right_block_idx:
                best_pair = left_block_len + right_block_len
            else:
                first_pair = left_block_len + blocks[left_block_idx + 1][0]
                last_pair = right_block_len + blocks[right_block_idx - 1][0]
                mid_pair = segment_tree.query(left_block_idx + 1, right_block_idx - 2)
                best_pair = max(first_pair, mid_pair, last_pair)

            ans.append(ones_count + best_pair)

        return ans


sol = Solution()
print(sol.maxActiveSectionsAfterTrade("01", [[0, 1]]))
print(sol.maxActiveSectionsAfterTrade("0100", [[0, 3], [0, 2], [1, 3], [2, 3]]))
print(sol.maxActiveSectionsAfterTrade("1000100", [[1, 5], [0, 6], [0, 4]]))
print(sol.maxActiveSectionsAfterTrade("01010", [[0, 3], [1, 4], [1, 3]]))
