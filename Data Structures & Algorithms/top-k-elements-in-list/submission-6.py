import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        vals = {}


        for i in nums:
            if i not in vals:
                vals[i] = 1
            else:
                vals[i] += 1
        
        
        max_heap = []

        for key, val in vals.items():
            max_heap.append((-1 * val, key))

        heapq.heapify(max_heap)

        answer = []

        for i in range(k):
            val = heapq.heappop(max_heap)
            answer.append(val[1])
        
        return answer



        


        