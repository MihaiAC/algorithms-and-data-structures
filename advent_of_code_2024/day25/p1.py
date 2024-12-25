class Solution:
    def __init__(self, input_file: str):
        input_lines = open(input_file).read().strip().split('\n')
        self.locks = []
        self.keys = []

        for idx in range(0, len(input_lines), 8):
            current_matrix = input_lines[idx:idx+7]
            curr_obj = []
            for col in range(5):
                curr_counter = 0
                for row in range(7):
                    if current_matrix[row][col] == '#':
                        curr_counter += 1
                curr_obj.append(curr_counter)

            if current_matrix[0] == '#####':
                self.locks.append(curr_obj)
            else:
                self.keys.append(curr_obj)
    
    def count_unique_valid_combos(self) -> int:
        count = 0
        for lock in self.locks:
            for key in self.keys:
                valid = True
                for idx in range(5):
                    if lock[idx] + key[idx] >= 8:
                        valid = False
                        break
                if valid:
                    count += 1
        return count

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.count_unique_valid_combos())


