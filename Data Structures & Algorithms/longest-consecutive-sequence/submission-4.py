class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        vals = set(nums)
        
        sequence = []

        for num in nums:
            if num - 1 not in vals:
                maxed = 1
                while num + 1 in vals:
                    maxed += 1
                    num += 1
            
                sequence.append(maxed)
                maxed = 0
        
        return max(sequence)

      
            


