"""
Problem 3. Longest Substring Without Repeating Characters
Category: Sliding Window
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Difficulty: Medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        unique_characters = set()
        for right in range(len(s)):
            while s[right] in unique_characters:
                unique_characters.remove(s[left])
                left += 1
            unique_characters.add(s[right])
            length = max(length, right - left + 1)
        return length


def test_plus_one():
    s = Solution()
    assert s.lengthOfLongestSubstring("zxyzxyz") == 3
    assert s.lengthOfLongestSubstring("xxxx") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3


if __name__ == "__main__":
    solver = Solution()

    result = solver.lengthOfLongestSubstring("dvdf")

    print(f"Result:    {result}")
