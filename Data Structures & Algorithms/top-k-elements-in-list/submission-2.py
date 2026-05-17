class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = []
        
        frequency = {}

        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
            
        for j in frequency.values():
            vals.append(j)
        
        vals.sort()

        vals = vals[-k:]

        answer = []
        for val in vals:
            for key, value in frequency.items():
                if value == val:
                    if key not in answer:
                        answer.append(key)
        
        return answer

        