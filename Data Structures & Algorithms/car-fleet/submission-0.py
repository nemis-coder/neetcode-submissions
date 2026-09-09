class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs_cars = [(pos,speed_curr) for pos, speed_curr in zip(position,speed)] 
        stack = []
        for pos, sp in sorted(pairs_cars,reverse=True):
            stack.append((target-pos)/sp)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)