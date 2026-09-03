class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frec_element = dict()
        for element in nums:
            frec_element[element] = frec_element.get(element,0) + 1
        items = sorted(frec_element.items(), key=lambda item: item[1], reverse=True) 
        solution = []
        for k,v in items[0:k]:
            solution.append(k)
        return solution