import heapq

class Solution:

    def distanceToOrigin(self, point: List[int])-> float:
        a = (0-point[0])**2
        b = (0-point[1])**2
        return math.sqrt(a+b)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_with_point = [ (self.distanceToOrigin(point),point) for point in points]
        solution = []
        print(distance_with_point)
        heapq.heapify(distance_with_point)
        for _ in range(k):
            smallest = heapq.heappop(distance_with_point)
            solution.append(smallest[1])
        return solution


