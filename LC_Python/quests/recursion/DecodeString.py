from typing import Tuple


class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)

        def _decodeString(idx: int) -> Tuple[str, int]:
            curr_str = []

            while idx < N:
                if s[idx].isalpha():
                    curr_str.append(s[idx])
                    idx += 1
                elif s[idx] == "]":
                    return ("".join(curr_str), idx + 1)
                else:
                    idx_open = s.find("[", idx + 1)
                    nrepeats = int(s[idx:idx_open])
                    inner_str, resume_idx = _decodeString(idx_open + 1)
                    curr_str.append(inner_str * nrepeats)
                    idx = resume_idx

            return "".join(curr_str), idx

        return _decodeString(0)[0]


sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("2[abc]3[cd]ef"))
