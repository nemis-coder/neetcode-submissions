class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_groups = {}
        for current_str in strs:
            sorted_in = ''.join(sorted(current_str))
            if sorted_in in map_groups:
                map_groups[sorted_in].append(current_str)
            else:
                map_groups[sorted_in] = [current_str]
        return list(map_groups.values())
