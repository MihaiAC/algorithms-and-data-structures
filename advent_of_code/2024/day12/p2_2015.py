import json

class Solution:
    def __init__(self, input_file):
        with open(input_file) as f:
            self.json = json.load(f)

    @staticmethod
    def calculate_sum(obj) -> int:
        current_sum = 0
        if isinstance(obj, dict):
            if "red" in obj.values():
                return 0
            for key in obj:
                current_sum += Solution.calculate_sum(obj[key])
        elif isinstance(obj, list):
            for elem in obj:
                current_sum += Solution.calculate_sum(elem)
        elif isinstance(obj, int):
            current_sum += obj
        return current_sum

if __name__ == '__main__':
    sol = Solution("input")
    print(Solution.calculate_sum(sol.json))
