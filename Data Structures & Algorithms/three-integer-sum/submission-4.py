class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        temp_answer = set()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if j < len(nums):
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = (nums[i], nums[j], nums[k])
                        temp_answer.add(t)
                        j += 1
                        k -=1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    
        answer = [list(i) for i in temp_answer]
        return answer

        
                