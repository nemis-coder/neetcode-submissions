class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_positions = {}
        for i in range(len(nums)):
            map_positions[nums[i]] = i
        for i in range(len(nums)):
            new_target = target - nums[i]
            if (new_target in map_positions) and map_positions[new_target]!=i:
                return [i, map_positions[new_target]]