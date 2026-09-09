class Solution:
    def computeHours(self, piles, k):
        total_hours = 0
        for pile in piles:
            consume_hours = math.ceil(pile/k)
            total_hours += consume_hours
        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = max(1, math.ceil(sum(piles)/h))
        r = max(piles)
        while(l<r):
            mid = (l+r)//2
            total_hours = self.computeHours(piles,mid)
            if total_hours>h:
                l = mid +1
            elif total_hours<=h:
                r = mid
        return l
