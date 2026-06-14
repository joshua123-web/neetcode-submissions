class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        vals = {}


        for i in nums:
            if i not in vals:
                vals[i] = 1
            else:
                vals[i] += 1
        
        sorter = []

        for key, val in vals.items():
            sorter.append((val, key))
        

        sorter.sort(reverse=True)

        j = 0

        answer = []

        for i in range(k):
            answer.append(sorter[j][1])
            j += 1

        return answer

        


        