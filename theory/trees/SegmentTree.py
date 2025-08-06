from typing import List

class SegmentTree:
    def __init__(self, arr: List[int], min_elem: int):
        self.N = len(arr)
        self.tree = [min_elem]*(4*self.N)
        self.min_elem = min_elem
        self.build(arr, 0, 0, self.N-1)

    def build(self, arr: List[int], curr_idx: int, left: int, right: int):
        if left == right:
            self.tree[curr_idx] = arr[left]
        else:
            middle = (left + right) // 2
            self.build(arr, 2*curr_idx+1, left, middle)
            self.build(arr, 2*curr_idx+2, middle+1, right)
            # TODO: replace with op.
            self.tree[curr_idx] = max(self.tree[2*curr_idx+1], self.tree[2*curr_idx+2])
    
    # TODO: Make it into an accum function.
    def query_max(self, query_left: int, query_right: int) -> int:
        return self._query_max(0, 0, self.N-1, query_left, query_right)
    
    def _query_max(self, curr_idx: int, segment_left: int, segment_right: int, query_left: int, query_right: int) -> int:
        if query_left > query_right:
            return self.min_elem

        if query_left == segment_left and query_right == segment_right:
            return self.tree[curr_idx]
    
        mid = (segment_left + segment_right) // 2

        return max(
            self._query_max(2 * curr_idx + 1, segment_left, mid, query_left, min(query_right, mid)),
            self._query_max(2 * curr_idx + 2, mid + 1, segment_right, max(query_left, mid + 1), query_right)
        )
    
    def update(self, pos: int, new_val: int):
        self._update(0, 0, self.N - 1, pos, new_val)

    def _update(
        self,
        curr_idx: int,
        segment_left: int,
        segment_right: int,
        pos: int,
        new_val: int
    ):
        if segment_left == segment_right:
            self.tree[curr_idx] = new_val
        else:
            mid = (segment_left + segment_right) // 2
            if pos <= mid:
                self._update(2 * curr_idx + 1, segment_left, mid, pos, new_val)
            else:
                self._update(2 * curr_idx + 2, mid + 1, segment_right, pos, new_val)
            self.tree[curr_idx] = max(
                self.tree[2 * curr_idx + 1],
                self.tree[2 * curr_idx + 2]
            )

if __name__ == '__main__':
    data = [2, 9, 3, 5, 7]
    st = SegmentTree(data, min_elem=0)

    # Query max in [1, 3].
    print("Max [1, 3]: ", st.query_max(1, 3))

    # Update index 2, then re-do the query.
    st.update(2, 10)
    print("After update, max[1, 3]: ", st.query_max(1, 3))