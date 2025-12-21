"""
Problem 66: Plus One
Category: Math
Link: https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            
        return [1] + digits
    
    
def test_plus_one():
    s = Solution()
    assert s.plusOne([1,2,3]) == [1,2,4]
    assert s.plusOne([4,3,2,1]) == [4,3,2,2]
    assert s.plusOne([9,9]) == [1,0,0]
    

    
    
if __name__ == "__main__":
    solver = Solution()
    
    result = solver.plusOne([1,2,3])

    print(f"Result:    {result}")