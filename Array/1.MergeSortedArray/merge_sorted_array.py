from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

if __name__ == "__main__":
    solver = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print(f"Initial array nums1: {nums1}")
    
    solver.merge(nums1, m, nums2, n)

    print(f"Result:    {nums1}")

    # Перевірка
    expected_output = [1, 2, 2, 3, 5, 6]
    print(f"Expected Result: {expected_output}")
    assert nums1 == expected_output
    print("Test passed successfully! ✅")