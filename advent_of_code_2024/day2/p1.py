class Solution:
    def calculate_n_safe_reports(self, input_file: str) -> int:
        n_safe_reports = 0
        with open(input_file) as f:
            for line in f:
                numbers = line.split(" ")
                increasing = int(numbers[1]) > int(numbers[0])
                prev = int(numbers[0])
                is_safe = True
                for num in numbers[1:]:
                    num = int(num)
                    if abs(num-prev) == 0 or abs(num-prev) > 3 or (num > prev) != increasing:
                        is_safe = False
                        break
                    prev = num
                if is_safe:
                    n_safe_reports += 1
        return n_safe_reports



if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate_n_safe_reports("input"))
