"""
Problem 33. Search in Rotated Sorted Array
Category: Binary Search
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else: 
                    start = mid + 1
        return -1


def test_plus_one():
    s = Solution()
    assert s.search([4,5,6,7,0,1,2], 0) == 4
    assert s.search([4,5,6,7,0,1,2], 3) == -1


if __name__ == "__main__":
    solver = Solution()

    result = solver.search([4,5,6,7,0,1,2], 0)

    print(f"Result:    {result}")
