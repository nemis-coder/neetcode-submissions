"""
nums = [2,3,1,1,5,5,4], k = 3

[1,1,2,3,4,5,5]

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
        