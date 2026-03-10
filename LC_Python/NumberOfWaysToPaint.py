MODN = 10**9 + 7


class Solution:
    def numOfWays(self, n: int) -> int:
        pattern_ABA = pattern_ABC = 6

        for _ in range(2, n + 1):
            pattern_ABA, pattern_ABC = (2 * pattern_ABA + 2 * pattern_ABC) % MODN, (
                2 * pattern_ABA + 3 * pattern_ABC
            ) % MODN

        return (pattern_ABA + pattern_ABC) % MODN
