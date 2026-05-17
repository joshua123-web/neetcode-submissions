class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        seen = set()
        while i < j:
            if heights[i] < heights[j]:
                value = heights[i] * (j - i)
                seen.add(value)
                i += 1
            elif heights[j] < heights[i]:
                value = heights[j] * (j - i)
                seen.add(value)
                j -= 1
            else:
                value = heights[i] * (j - i)
                seen.add(value)
                i += 1
                j -= 1
        m = max(seen)

        return m
        
