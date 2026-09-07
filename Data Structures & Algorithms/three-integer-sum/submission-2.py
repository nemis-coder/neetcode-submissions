"""
We can consider the following: 
nums[i] + nums[j] + nums[k] == 0

We can convert the problem to the following: 
nums[i] + nums[j] == nums[k]

The solution should not contain any duplicates. 

We can create a set:

dict_nums = {}

for i in len(nums):
    dict_nums.get(i,[]).append(i)

Now each key in dict_nums can be used as nums[k]

for key in dict_nums.keys():
    twoSum(dict_nums,target=key)

def twoSum(dict_nums, target=key):
    for key in dict_nums:
        new_target = target-key

"""
class Solution:
    solutions = set()
    def validDicts(self, dict_to_valid, dict_org):
        for comp_key in dict_to_valid.keys():
            if dict_to_valid[comp_key] > dict_org.get(comp_key,0):
                return False
        return True

    def twoSum(self,dict_frecs,target):
        for i in dict_frecs.keys():
            current_dict = dict()
            j = target - i
            current_dict[-target] = current_dict.get(-target,0) + 1
            current_dict[i] = current_dict.get(i,0) + 1
            current_dict[j] = current_dict.get(j,0) + 1
            if self.validDicts(current_dict,dict_frecs):
                list_val = tuple(sorted([-target,i,j]))
                self.solutions.add(list_val)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.solutions = set()
        dict_frecs = dict()
        for num in nums:
            dict_frecs[num] = dict_frecs.get(num,0) + 1
        for k in dict_frecs.keys():
            self.twoSum(dict_frecs,-k)
        solution = [list(x) for x in self.solutions]
        return solution
