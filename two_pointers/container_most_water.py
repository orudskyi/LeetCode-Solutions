"""
11. Container With Most Water
Category: Two Pointers
Link: https://leetcode.com/problems/container-with-most-water/description/
Difficulty: Medium
"""


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        start = 0
        end = len(heights) - 1
        res = 0
        
        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            res = max(res, area)
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return res


def test_plus_one():
    s = Solution()
    assert s.maxArea([1, 7, 2, 5, 4, 7, 3, 6]) == 36
    assert s.maxArea([2, 2, 2]) == 4


if __name__ == "__main__":
    solver = Solution()

    result = solver.maxArea([1, 7, 2, 5, 4, 7, 3, 6])

    print(f"Result:    {result}")
