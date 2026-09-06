class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ind = 0
        right_ind = len(numbers)-1
        while(left_ind<right_ind):
            current_sum = numbers[left_ind] + numbers[right_ind]
            if current_sum>target:
                right_ind-=1
            elif current_sum<target:
                left_ind+=1
            else:
                return [left_ind+1,right_ind+1]
        return []