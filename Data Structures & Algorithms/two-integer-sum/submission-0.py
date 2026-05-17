class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in checker:
                answer = [checker[difference], i]
            else:
                checker[nums[i]] = i
        return answer
                
