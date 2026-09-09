"""
We need to implement the binary search algorithm.
The idea is compute the number in the middle.
mid = (r-l)/2 In this scenario we need to consider 
the overflow that can happen.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

