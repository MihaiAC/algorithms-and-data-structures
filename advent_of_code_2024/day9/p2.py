from sortedcontainers import SortedList

class Solution:
    def __init__(self, input_file: str):
        with open(input_file) as f:
            for line in f:
                self.line = line
    
    def calculate_checksum(self) -> int:
        # (length, idx, counter)
        empty_blocks = SortedList([])

        # (order_auxval1, order_auxval2, value(id), length)
        non_empty_blocks = SortedList([])

        # (idx, length).
        non_empty_blocks_initial = []
        for idx in range(len(self.line)):
            if idx % 2 == 1:
                empty_blocks.add((int(self.line[idx]), idx, 0))
            else:
                non_empty_blocks_initial.append((idx, int(self.line[idx])))
        
        # For every non-empty block, from right to left, 
        # try to find an empty block to match it with.
        while len(non_empty_blocks_initial) > 0:
            non_empty_block_idx, non_empty_block_length = non_empty_blocks_initial.pop()
            non_empty_block_ID = non_empty_block_idx // 2
            empty_block_idx = empty_blocks.bisect_left((non_empty_block_length, -float('inf'), -float('inf')))
            if empty_block_idx == len(empty_blocks):
                non_empty_blocks.add((non_empty_block_idx, 0, non_empty_block_ID, non_empty_block_length))
            else:
                leftmost_idx = float('inf')
                value_with_leftmost_idx = None
                for value in empty_blocks.islice(empty_block_idx):
                    if value[1] < leftmost_idx:
                        leftmost_idx = value[1]
                        value_with_leftmost_idx = value
                
                # Empty block needs to be to the left of the non-empty block we're
                # trying to shift left.
                if non_empty_block_idx > leftmost_idx:
                    empty_blocks.remove(value_with_leftmost_idx)
                    empty_block_length, empty_block_idx, empty_block_counter = value_with_leftmost_idx
                    non_empty_blocks.add((empty_block_idx, empty_block_counter, non_empty_block_ID, non_empty_block_length))
                    empty_blocks.add((non_empty_block_length, non_empty_block_idx, 0))
                    
                    # Check if there are still empty blocks left.
                    if non_empty_block_length < empty_block_length:
                        empty_blocks.add((empty_block_length-non_empty_block_length, empty_block_idx, empty_block_counter+1))
                else:
                    non_empty_blocks.add((non_empty_block_idx, 0, non_empty_block_ID, non_empty_block_length))
        
        # Add remaining empty blocks to non-empty blocks with an id of 0.
        for (empty_block_length, empty_block_idx, empty_block_counter) in empty_blocks.islice():
            non_empty_blocks.add((empty_block_idx, empty_block_counter+1, 0, empty_block_length))

        checksum = 0
        curr_idx = 0
        res = []
        for (_, _, block_id, length) in non_empty_blocks.islice():
            for _ in range(length):
                res.append(str(block_id))
                checksum += block_id * curr_idx
                curr_idx += 1
        
        return checksum


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_checksum())