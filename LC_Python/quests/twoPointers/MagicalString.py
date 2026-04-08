inverse = {"1": "2", "2": "1"}


class Solution:
    def magicalString(self, n: int) -> int:
        string = ["1", "2", "2"]
        idx = 2
        while len(string) < n:
            string += [inverse[string[-1]]] * (int(string[idx]))
            idx += 1

        return sum([1 if x == "1" else 0 for x in string[:n]])


if __name__ == "__main__":
    sol = Solution()

    s1 = sol.magicalString(6)
    assert s1 == 3, f"expected 3, actual {s1}"

    s2 = sol.magicalString(1)
    assert s2 == 1, f"expected 1, actual {s2}"
