from sys import argv

class Solution:
    def numSquares(self, n: int) -> int:
        next_square = 4
        next_root_square = 2
        perfect_squares = [1]
        num_squares = [0, 1]

        for ii in range(2, n+1):
            if ii == next_square:
                num_squares.append(1)
                perfect_squares.append(next_square)
                next_root_square += 1
                next_square = next_root_square**2
            else:
                min_num_squares = 5
                for square in perfect_squares:
                    candidate = num_squares[ii-square]+1
                    if min_num_squares > candidate:
                        min_num_squares = candidate
                        if candidate == 2:
                            break
                num_squares.append(min_num_squares)
        
        print(num_squares)
        return num_squares[n]

if __name__ == '__main__':
    n = int(argv[1])
    sol = Solution()
    print(sol.numSquares(n))