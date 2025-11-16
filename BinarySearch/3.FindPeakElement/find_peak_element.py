from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid

            else:
                left = mid + 1

        return right


if __name__ == "__main__":
    solver = Solution()

    # 1. Збираємо ВСІ тестові випадки в один список
    # Кожен випадок - це (matrix, target, expected_result)
    test_cases = [
        ([1, 2, 3, 1], 2),  # Тест 1
        ([1, 2, 1, 3, 5, 6, 4], 5),  # Тест 2
    ]

    print("Running tests...")

    # 2. Запускаємо один цикл, який пройде по всіх тестах
    # enumerate дає нам номер тесту "i" (0, 1, 2...)
    for i, (matrix, expected) in enumerate(test_cases):
        result = solver.findPeakElement(matrix)

        try:
            assert result == expected
            # 3. Друкуємо результат для кожного тесту
            print(f"Test #{i + 1} PASSED ✅")
        except AssertionError:
            # 4. Якщо тест впав, ми побачимо детальну помилку
            print(f"Test #{i + 1} FAILED ❌")
            print(f"  Input matrix: {matrix}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            print("-" * 20)

    print("\nAll tests finished.")
