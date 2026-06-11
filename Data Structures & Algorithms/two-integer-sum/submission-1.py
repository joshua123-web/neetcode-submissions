class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        vals = {}

        
        
        for i in range(len(nums)):
            vals[i] = target - nums[i]
        


        for key, val in vals.items():

            if val in nums:
                answer = [key, nums.index(val)]
        
        answer.sort()

        return answer