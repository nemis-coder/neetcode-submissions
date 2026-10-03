import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while(len(max_heap)>1):
            first_rock = -heapq.heappop(max_heap)
            second_rock = -heapq.heappop(max_heap)
            if first_rock != second_rock:
                new_rock = first_rock - second_rock
                heapq.heappush(max_heap,-new_rock)
        if len(max_heap)>0:
            return -max_heap[0]
        return 0
        