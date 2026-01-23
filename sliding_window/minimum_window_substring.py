"""
Problem 76. Minimum Window Substring
Category: Sliding Window
Link: https://neetcode.io/problems/minimum-window-with-characters/question
Difficulty: Hard
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l = 0
        have = 0
        need = len(countT)
        res = [-1, -1]
        reslen = float("inf")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if reslen == float("inf"):
            return ""
        return s[l : r + 1]


def test_plus_one():
    s = Solution()
    assert s.minWindow("OUZODYXAZV", "XYZ") == "YXAZ"
    assert s.minWindow("xyz", "xyz") == "xyz"
    assert s.minWindow("x", "xy") == ""


if __name__ == "__main__":
    solver = Solution()

    result = solver.minWindow("OUZODYXAZV", "XYZ")

    print(f"Result:    {result}")
