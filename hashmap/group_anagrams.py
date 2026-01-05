"""
Problem 49. Group Anagrams
Category: Hashmap
Link: https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Medium
"""

from typing import List
from collections import defaultdict

class Solution:  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_key = "".join(sorted(word))
            
            anagram_map[sorted_key].append(word)
            
        return list(anagram_map.values())  
    
def test_plus_one():
    s = Solution()
    assert s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    
if __name__ == "__main__":
    solver = Solution()
    
    result = solver.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

    print(f"Result:    {result}")