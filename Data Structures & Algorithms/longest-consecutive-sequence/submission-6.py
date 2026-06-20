class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        vals = set(nums)
        longest = 0
        for i in vals:
            
            count = 1
            x = i
            if x - 1 not in vals:
                
                while x + 1 in vals:
                    x += 1
                    count += 1
            
            longest = max(longest, count)

        
        return longest
        
                

       
            
        
      
            


