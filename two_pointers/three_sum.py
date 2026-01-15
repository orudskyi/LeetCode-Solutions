"""
15. 3Sum
Category: Two Pointers
Link: https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


def test_plus_one():
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([0, 1, 1]) == []


if __name__ == "__main__":
    solver = Solution()

    result = solver.threeSum([-1, 0, 1, 2, -1, -4])

    print(f"Result:    {result}")
