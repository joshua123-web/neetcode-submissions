class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        i = 0
        j = len(nums) - 1
        vals = 0
        for i in nums:
            vals ^= i

        
        return vals



