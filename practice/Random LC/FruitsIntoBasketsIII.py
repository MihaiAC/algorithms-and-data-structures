class SegmentTree:
    def __init__(self, arr: List[int], min_elem: int):
        self.N = len(arr)
        self.tree = [min_elem] * (4 * self.N)
        self.min_elem = min_elem
        self.build(arr, curr_idx=0, segment_left=0, segment_right=self.N - 1)

    def build(
        self,
        arr: List[int],
        curr_idx: int,
        segment_left: int,
        segment_right: int
    ):
        if segment_left == segment_right:
            self.tree[curr_idx] = arr[segment_left]
        else:
            mid = (segment_left + segment_right) // 2
            self.build(arr, 2*curr_idx + 1, segment_left, mid)
            self.build(arr, 2*curr_idx + 2, mid + 1, segment_right)
            self.tree[curr_idx] = max(
                self.tree[2*curr_idx + 1],
                self.tree[2*curr_idx + 2]
            )

    def find_first(
        self,
        curr_idx: int,
        segment_left: int,
        segment_right: int,
        x: int
    ) -> int:
        if self.tree[curr_idx] < x:
            return -1
        
        if segment_left == segment_right:
            return segment_left
        
        mid = (segment_left + segment_right) // 2
        left_child = 2*curr_idx + 1
        
        if self.tree[left_child] >= x:
            return self.find_first(left_child, segment_left, mid, x)
        
        return self.find_first(left_child + 1, mid + 1, segment_right, x)

    def update(
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
                self.update(2*curr_idx + 1, segment_left, mid, pos, new_val)
            else:
                self.update(2*curr_idx + 2, mid + 1, segment_right, pos, new_val)
            self.tree[curr_idx] = max(
                self.tree[2*curr_idx + 1],
                self.tree[2*curr_idx + 2]
            )

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets, 0)
        unplaced = 0

        for fruit in fruits:
            pos = st.find_first(0, 0, len(baskets)-1, fruit)

            if pos == -1:
                unplaced += 1
            else:
                st.update(0, 0, len(baskets)-1, pos, 0)
        
        return unplaced