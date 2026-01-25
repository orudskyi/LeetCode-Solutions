"""
739. Daily Temperatures
Category: Stack
Link: https://neetcode.io/problems/daily-temperatures/question
Difficulty: Medium
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            
            if j < n:
                res[i] = j - i
        return res


def test_plus_one():
    s = Solution()
    assert s.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]) == [1, 4, 1, 2, 1, 0, 0]
    assert s.dailyTemperatures([22, 21, 20]) == [0, 0, 0]


if __name__ == "__main__":
    solver = Solution()

    result = solver.dailyTemperatures([30, 38, 30, 36, 35, 40, 28])

    print(f"Result:    {result}")
