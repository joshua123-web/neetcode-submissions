class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =  set()

        i = 0
        j = len(prices) - 1
        maxed = len(prices) - 1

        while i != maxed:
            while i != j:
                max_profit.add(prices[j] - prices[i])
                j -= 1
            j = len(prices) - 1
            i += 1
        
        if not max_profit:
            return 0

        if max(max_profit) > 0:
            return max(max_profit)
        else:
            return 0



        
            