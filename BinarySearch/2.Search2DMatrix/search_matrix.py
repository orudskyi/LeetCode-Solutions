from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        left, right = 0, len(matrix[0]) - 1

        for i in range(len(matrix)):
            if target == matrix[i][right]:
                return True

            if target < matrix[i][right]:
                while left <= right:
                    mid = left + (right - left) // 2

                    if matrix[i][mid] == target:
                        return True

                    if matrix[i][mid] < target:
                        left = mid + 1

                    else:
                        right = mid - 1

                return False

        return False


if __name__ == "__main__":
    solver = Solution()

    # 1. Збираємо ВСІ тестові випадки в один список
    # Кожен випадок - це (matrix, target, expected_result)
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),  # Тест 1
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False), # Тест 2
        ([[1], [3]], 3, True),                                        # Тест 3 (твій проблемний)
        ([[1], [3]], 1, True),                                        # Тест 4 (додамо ще один)
        ([[1, 2], [3, 4]], 5, False),                                 # Тест 5
        ([[]], 1, False),                                             # Тест 6 (крайній випадок)
        ([], 1, False),                                               # Тест 7 (крайній випадок)
    ]

    print("Running tests...")
    
    # 2. Запускаємо один цикл, який пройде по всіх тестах
    # enumerate дає нам номер тесту "i" (0, 1, 2...)
    for i, (matrix, target, expected) in enumerate(test_cases):
        result = solver.searchMatrix(matrix, target)
        
        try:
            assert result == expected
            # 3. Друкуємо результат для кожного тесту
            print(f"Test #{i + 1} PASSED ✅")
        except AssertionError:
            # 4. Якщо тест впав, ми побачимо детальну помилку
            print(f"Test #{i + 1} FAILED ❌")
            print(f"  Input matrix: {matrix}")
            print(f"  Input target: {target}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            print("-" * 20)

    print("\nAll tests finished.")
