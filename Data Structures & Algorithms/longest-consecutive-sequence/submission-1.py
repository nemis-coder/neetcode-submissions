"""
Is expected to solve this problem in O(n)
but lets explore other alternatives. 
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #What happen if we sort the list of nums?
        if(len(nums)==0):
            return 0
        nums_sorted = sorted(list(set(nums)))
        print(nums_sorted)
        current_size = 1
        max_current_size = -1
        for i in range(0,len(nums_sorted)-1):
            if nums_sorted[i]+1 == nums_sorted[i+1]:
                current_size += 1
            else:
                max_current_size= max(current_size,max_current_size)
                current_size = 1
        max_current_size= max(current_size,max_current_size)
        return max_current_size




