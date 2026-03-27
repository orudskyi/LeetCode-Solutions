"""
Problem 703. Kth Largest Element in a Stream
Category: Heap
Link: https://neetcode.io/problems/search-for-word-ii/question
Difficulty: Hard
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


if __name__ == "__main__":
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print(kthLargest.add(3))  # return 3
    print(kthLargest.add(5))  # return 3
    print(kthLargest.add(6))  # return 3
    print(kthLargest.add(7))  # return 5
    print(kthLargest.add(8))  # return 6
