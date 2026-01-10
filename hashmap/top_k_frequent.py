"""
Problem 347. Top K Frequent Elements
Category: Hashmap
Link: https://leetcode.com/problems/top-k-frequent-elements/description/
Difficulty: Medium
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
        sorted_items = sorted(count_map.items(), key=lambda item: item[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
            
        return result


def test_plus_one():
    s = Solution()
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]


if __name__ == "__main__":
    solver = Solution()

    result = solver.topKFrequent([1, 1, 1, 2, 2, 3], 2)

    print(f"Result:    {result}")
