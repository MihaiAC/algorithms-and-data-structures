from typing import List


class Solution:
    def validateCoupons(
        self, codes: List[str], business_lines: List[str], is_active: List[bool]
    ) -> List[str]:
        N = len(codes)
        ans = []

        for idx in range(N):
            code = codes[idx]

            if len(code) == 0:
                continue

            if not all(c.isalnum() or c == "_" for c in code):
                continue

            active = is_active[idx]
            if not active:
                continue

            business = business_lines[idx]
            if business not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                continue

            ans.append((code, business, active))

        return [x[0] for x in sorted(ans, key=lambda y: (y[1], y[0]))]
