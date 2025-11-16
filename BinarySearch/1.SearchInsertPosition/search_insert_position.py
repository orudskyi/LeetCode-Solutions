class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
    
if __name__ == "__main__":
    solver = Solution()

    nums = [1, 3, 5, 6]
    target1 = 5
    target2 = 2
    target3 = 7

    print(f"Initial array nums1: {nums}")
    
    result = solver.searchInsert(nums, target3)

    print(f"Result:    {result}")

    # Перевірка
    expected_output = 4
    print(f"Expected Result: {expected_output}")
    assert result == expected_output
    print("Test passed successfully! ✅")