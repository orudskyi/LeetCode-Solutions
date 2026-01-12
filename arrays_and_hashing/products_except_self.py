"""
Problem 238. Product of Array Except Self
Category: Arrays and Hashing
Link: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * (len(nums))
        
        pref = 1
        for i in range(len(nums)):
            result[i] = pref
            pref *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
        return result


def test_plus_one():
    s = Solution()
    assert s.productExceptSelf([1, 2, 4, 6]) == [48, 24, 12, 8]
    assert s.productExceptSelf([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]


if __name__ == "__main__":
    solver = Solution()

    result = solver.productExceptSelf([1, 2, 4, 6])

    print(f"Result:    {result}")
