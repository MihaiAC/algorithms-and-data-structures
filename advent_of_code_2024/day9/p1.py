class Solution:
    def __init__(self, input_file: str):
        with open(input_file) as f:
            for line in f:
                self.line = line
    
    def calculate_checksum(self) -> int:
        left_lidx = 0
        right_lidx = len(self.line)
        right_remaining_repeats = 0
        right_current_id = -1
        block_idx = 0
        checksum = 0

        while left_lidx < right_lidx:
            if left_lidx % 2 == 0:
                file_id = left_lidx // 2
                repeats = int(self.line[left_lidx])
                for _ in range(repeats):
                    # print(f"(Left block) Index: {block_idx}, number: {file_id}")
                    checksum += block_idx * file_id
                    block_idx += 1
                left_lidx += 1
            else:
                empty_blocks = int(self.line[left_lidx])
                for _ in range(empty_blocks):
                    if right_remaining_repeats == 0:
                        right_lidx -= 1
                        if right_lidx % 2 == 1:
                            right_lidx -= 1
                        right_remaining_repeats = int(self.line[right_lidx])
                        right_current_id = right_lidx // 2
                    
                    if left_lidx >= right_lidx:
                        break
                    
                    # print(f"(Filling empty) Index: {block_idx}, number: {right_current_id}")
                    checksum += block_idx * right_current_id
                    right_remaining_repeats -= 1
                    block_idx += 1
                left_lidx += 1
        
        for _ in range(right_remaining_repeats):
            checksum += block_idx * right_current_id
            # print(f"(FINAL) Index: {block_idx}, number: {right_current_id}")
            block_idx += 1
        
        return checksum



if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_checksum())