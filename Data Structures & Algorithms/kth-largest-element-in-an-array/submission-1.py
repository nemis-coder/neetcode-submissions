"""
nums = [2,3,1,1,5,5,4], k = 3

[1,1,2,3,4,5,5]

"""
import heapq

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(k):
           heapq.heappush(min_heap,nums[i]) 

        for i in range(k,len(nums)):
            if nums[i]< min_heap[0]:
                continue
            else:
                heapq.heapreplace(min_heap,nums[i])
                
        return min_heap[0]



        