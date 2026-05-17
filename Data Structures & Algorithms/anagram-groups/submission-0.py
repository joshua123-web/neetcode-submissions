class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        vals = {}
        result = []
        for val in strs:
            sorted_val = "".join(sorted(val))
            if sorted_val not in seen:
                seen.add(sorted_val)
                vals[sorted_val] = [val]
            else:
                vals[sorted_val].append(val)
        
        for item in vals.values():
            result.append(item)
        
        return result

      

