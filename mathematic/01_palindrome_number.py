"""
Problem 9: Palindrome Number
Category: AMath
Link: https://leetcode.com/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x = x // 10
            
        return x == reversed_half or x == reversed_half // 10    
    
    
def test_palindrome_number():
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    
    
    
    
if __name__ == "__main__":
    solver = Solution()
    
    result = solver.isPalindrome(121)

    print(f"Result:    {result}")