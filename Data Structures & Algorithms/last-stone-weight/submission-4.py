import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]

        heapq.heapify(stones)


        while stones:

            if len(stones) == 1:
                return -stones[0]
            
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x > y:
                j = x - y
                heapq.heappush(stones, -j)

        return 0