class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = float('inf')
        if(len(nums))<=2: 
            return min(nums)
        while(l<=r):
            mid = (r+l)//2
            if nums[mid]<=nums[r]:
                min_val = min(nums[mid],min_val)
                r = mid - 1
            elif nums[mid]>=nums[l]:
                min_val = min(nums[l],min_val)
                l = mid +1
        return min_val

