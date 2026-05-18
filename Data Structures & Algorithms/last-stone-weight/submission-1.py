class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        elif len(stones) == 1:
            return stones[0]
        
        stones.sort()

        while len(stones) > 1:
            x = stones[-1]
            y = stones[-2]

            if x == y:
                stones.pop()
                stones.pop()
            elif x > y:
                stones.pop()
                stones.pop()
                stones.append(x - y)
                stones.sort()
            
        if stones:
            return stones[0]
        else:
            return 0
            