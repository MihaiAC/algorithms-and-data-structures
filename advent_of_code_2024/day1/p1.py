import heapq

class Solution:
    def calculate_distance(self, input_file: str) -> int:
        heap1, heap2 = [], []
        with open(input_file) as file:
            for line in file:
                numbers = line.split("   ")
                heapq.heappush(heap1, int(numbers[0]))
                heapq.heappush(heap2, int(numbers[1]))
        
        distance = 0
        for _ in range(len(heap1)):
            n1 = heapq.heappop(heap1)
            n2 = heapq.heappop(heap2)
            distance += abs(n1-n2)
        
        return distance

if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate_distance('input'))