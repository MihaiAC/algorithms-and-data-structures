from typing import List
from collections import defaultdict, deque

MAXN = 10**6 + 1

is_prime = [True] * MAXN
is_prime[0] = False
is_prime[1] = False

for num in range(2, MAXN):
    if is_prime[num]:
        for mult in range(2 * num, MAXN, num):
            is_prime[mult] = False


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        primes = set([x for x in nums if is_prime[x]])

        buckets = defaultdict(list)
        for idx, num in enumerate(nums):
            for prime in primes:
                if num % prime == 0:
                    buckets[prime].append(idx)

        N = len(nums)
        jumps = 0

        visited = [False] * N
        visited[0] = True

        queue = deque()
        queue.appendleft(0)

        while len(queue) > 0:
            for _ in range(len(queue)):
                curr_idx = queue.pop()

                if curr_idx == N - 1:
                    return jumps

                # Enqueue neighbors
                if curr_idx > 0 and curr_idx - 1 and not visited[curr_idx - 1]:
                    queue.appendleft(curr_idx - 1)
                    visited[curr_idx - 1] = True

                if curr_idx + 1 and not visited[curr_idx + 1]:
                    queue.appendleft(curr_idx + 1)
                    visited[curr_idx + 1] = True

                # Enqueue multiples if nums[curr_idx] is a prime.
                num = nums[curr_idx]
                if is_prime[num]:
                    for multiple in buckets[num]:
                        if not visited[multiple]:
                            queue.appendleft(multiple)
                            visited[multiple] = True
                    del buckets[num]

            jumps += 1

        return jumps


sol = Solution()
print(sol.minJumps([1, 2, 4, 6]))
print(sol.minJumps([2, 3, 4, 7, 9]))
print(sol.minJumps([4, 6, 5, 8]))
print(sol.minJumps([7, 5, 7]))
