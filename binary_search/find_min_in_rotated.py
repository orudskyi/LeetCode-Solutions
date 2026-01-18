"""
Problem 153. Find Minimum in Rotated Sorted Array
Category: Binary Search
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        return nums[start]
    
    
    
def test_plus_one():
    s = Solution()
    assert s.findMin([3,4,5,6,1,2]) == 1
    assert s.findMin([4,5,0,1,2,3]) == 0
    
    
    
if __name__ == "__main__":
    solver = Solution()
    
    result = solver.findMin([4,5,0,1,2,3])

    print(f"Result:    {result}")