class Solution:
    def isInterval(self,low,up,val):
        return low<=val and val<=up
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l<=r):
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>=nums[l]:
                if self.isInterval(nums[l],nums[mid],target):
                    r = mid
                else:
                    l = mid + 1
            elif nums[mid]<=nums[r]:
                if self.isInterval(nums[mid],nums[r],target):
                    l = mid
                else:
                    r = mid -1
        return -1

        