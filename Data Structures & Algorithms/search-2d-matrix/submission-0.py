class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1  
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target  and row[-1]>=target:
                find_element = self.binarySearch(row,target)
                if find_element:
                    return True
        return False
            