"""
Problem 128. Longest Consecutive Sequence
Category: HashMap
Link: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) in num_set:
                continue
            i = 1
            while (num + i) in num_set:
                i += 1
            if i > max_len:
                max_len = i
        return max_len


def test_plus_one():
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([1, 0, 1, 2]) == 3


if __name__ == "__main__":
    solver = Solution()

    result = solver.longestConsecutive([100, 4, 200, 1, 3, 2])

    print(f"Result:    {result}")
