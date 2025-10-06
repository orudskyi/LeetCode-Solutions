from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #result = {}
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
                    

if __name__ == "__main__":
    solver = Solution()

    nums = [3, 3]
    target = 6

    print(f"Initial array nums1: {nums}")
    
    result = solver.twoSum(nums, target)

    print(f"Result:    {result}")

    expected_output = [0, 1]
    print(f"Expected Result: {expected_output}")
    assert result == expected_output
    print("Test passed successfully! ✅")