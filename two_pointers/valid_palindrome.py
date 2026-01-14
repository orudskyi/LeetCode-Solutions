"""
Problem 125. Valid Palindrome
Category: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        start = 0
        end = len(s) - 1
        
        while (start < end):
            while start < end and not s[start].isalnum():
                start += 1
                
            while end > start and not s[end].isalnum():
                end -= 1
            
            if s[start].lower() != s[end].lower():
                return False 
            
            start += 1
            end -= 1
        
        return True
    
    
def test_plus_one():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama")
    assert not s.isPalindrome("race a car")
    
    
    
if __name__ == "__main__":
    solver = Solution()
    
    result = solver.isPalindrome("A man, a plan, a canal: Panama")

    print(f"Result:    {result}")