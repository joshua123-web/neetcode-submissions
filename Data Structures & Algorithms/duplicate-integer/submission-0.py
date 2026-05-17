class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}

        for val in nums:
            if val not in vals:
                vals[val] = 1
            else:
                return True
        return False