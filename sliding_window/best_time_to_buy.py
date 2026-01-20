"""
Problem 121. Best Time to Buy and Sell Stock
Category: Sliding Window
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit


def test_plus_one():
    s = Solution()
    assert s.maxProfit([10, 1, 5, 6, 7, 1]) == 6
    assert s.maxProfit([10, 8, 7, 5, 2]) == 0


if __name__ == "__main__":
    solver = Solution()

    result = solver.maxProfit([10, 1, 5, 6, 7, 1])

    print(f"Result:    {result}")
