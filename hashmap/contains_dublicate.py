"""
Problem 217. Contains Duplicate
Category: HashMap
Link: https://leetcode.com/problems/contains-duplicate/description/
Difficulty: Easy
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
     
def test_plus_one():
    s = Solution()
    assert s.hasDuplicate([1,2,3,3])
    assert not s.hasDuplicate([1,2,3,4])
    
    
    
if __name__ == "__main__":
    solver = Solution()
    
    result = solver.hasDuplicate([1,2,3,4])

    print(f"Result:    {result}")