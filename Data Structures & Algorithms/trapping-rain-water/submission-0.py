class Solution:
    def trap(self, height: List[int]) -> int:
        suffix = [ 0 for _ in range(len(height))]
        preffix = [ 0 for _ in range(len(height))]
        suffix[0] = height[0]
        preffix[-1] = height[-1]
        for i in range(1,len(height)):
            suffix[i] = max(suffix[i-1],height[i])
            preffix[-1-i] = max(preffix[-i],height[-1-i])
        total = 0
        for i in range(1,len(height)):
            current_h = min(suffix[i],preffix[i])
            current_capacity = current_h - height[i] 
            if current_capacity>0:
                total+= current_capacity
        return total
        