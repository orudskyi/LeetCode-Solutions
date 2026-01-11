"""
Problem 242. Valid Anagram
Category: Hashmap
Link: https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        
        for char in s:
            counter[char] = counter.get(char, 0) + 1
            
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        
        return True
        
    
    
def test_plus_one():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram")
    assert not s.isAnagram("rat", "car")
    
    
if __name__ == "__main__":
    solver = Solution()
    
    result = solver.isAnagram("anagram", "nagaram")

    print(f"Result:    {result}")