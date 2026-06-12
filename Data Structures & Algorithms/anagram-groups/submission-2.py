class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        vals = {}

        for i in strs:
            letters = sorted(i)
            k = ''.join(letters)
            if k not in vals:
                vals[k] = [i]
            else:
                vals[k].append(i)
        
        answer = []

        for value in vals.values():
            answer.append(value)

        
        return answer
            
      

