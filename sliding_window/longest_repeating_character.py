"""
Problem 424. Longest Repeating Character Replacement
Category: Sliding Window
Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/
Difficulty: Medium
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)

        return result


def test_plus_one():
    s = Solution()
    assert s.characterReplacement("XYYX", 2) == 4
    assert s.characterReplacement("AAABABB", 1) == 5
    assert s.characterReplacement("XYXYX", 2) == 5


if __name__ == "__main__":
    solver = Solution()

    result = solver.characterReplacement("XYYX", 2)

    print(f"Result:    {result}")
