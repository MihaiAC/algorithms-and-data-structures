# Couldn't come up with a solution, just trying to understand the editorial...

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        N = len(s)
        # left[ii][0] = number of partitions in [0, ii-1]
        # left[ii][1] = characters in the last partition in [0, ii-1]
        left = [[0]*2 for _ in range(N)]

        # right[ii][0] = number of partitions in [ii+1, N]
        # right[ii][1] = characters in the first partition in [ii+1, N]
        right = [[0]*2 for _ in range(N)]

        num_partitions = 0 # number of partitions found so far
        mask = 0 # represents characters in the current partition
        count = 0 # number of different characters in the current partition

        for ii in range(N-1):
            char_bin = 1 << (ord(s[ii])-ord('a'))
            if not (char_bin & mask):
                # Curr char is not in the curr partition.
                count += 1
                if (count <= k):
                    mask = mask | char_bin # add char to the mask
                else:
                    num_partitions += 1 # previous partition is over
                    mask = char_bin
                    count = 1
            
            left[ii+1][0] = num_partitions
            left[ii+1][1] = mask
        
        # Same as above, but for right.
        num_partitions, mask, count = 0, 0, 0
        for ii in range(N-1, 0, -1):
            char_bin = 1 << (ord(s[ii]) - ord('a'))
            if not (char_bin & mask):
                count += 1
                if count <= k:
                    mask |= char_bin
                else:
                    num_partitions += 1
                    mask = char_bin
                    count = 1
            right[ii-1][0] = num_partitions
            right[ii-1][1] = mask

        max_partitions = 0
        for ii in range(N):
            # I think by default we assume that both the left partition
            # and the right partition are unfinished and adding a new char 
            # finishes them both somehow.
            curr_partitions = left[ii][0] + right[ii][0] + 2
            mask = left[ii][1] | right[ii][1]
            count = mask.bit_count()

            if left[ii][1].bit_count() == k and right[ii][1].bit_count() == k and count < 26:
                # In this case, I guess we finish both left and right partitions
                # and we create one new one at least(?).
                curr_partitions += 1
            elif min(count+1, 26) <= k:
                # Left and right can be merged into a single extra partition. 
                curr_partitions -= 1
            
            max_partitions = max(max_partitions, curr_partitions)
        
        return max_partitions 

        
if __name__ == '__main__':
    sol = Solution()
    s = "xxyz"
    k = 1

    print(sol.maxPartitionsAfterOperations(s, k))