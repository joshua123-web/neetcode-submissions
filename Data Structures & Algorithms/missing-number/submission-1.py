class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        j = len(nums)
        
        seen = set(nums)

        for i in range(0, j + 1):
            if i not in seen:
                return i