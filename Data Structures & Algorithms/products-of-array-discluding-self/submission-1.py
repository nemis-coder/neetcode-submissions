class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [nums[0]]
        suffix_product = [0 for x in range(len(nums))]
        solution = [0 for x in range(len(nums))]
        suffix_product[-1] = nums[-1]
        for i in range(1,len(nums)):
            prefix_product.append(prefix_product[i-1]*nums[i])
        for j in range(len(nums)-2,-1,-1):
            suffix_product[j] = suffix_product[j+1]*nums[j]
        #print(prefix_product, suffix_product)
        for i in range(0,len(nums)):
            prefix_current = prefix_product[i-1] if i-1>=0 else 1
            suffix_current = suffix_product[i+1] if i+1<len(suffix_product) else 1
            #print(prefix_current,suffix_current)
            solution[i] = prefix_current*suffix_current
        return solution
