class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        

        i = 0

        mapper1 = {}

        mapper2 = {}


        while i < len(s):
            if s[i] not in mapper1:
                mapper1[s[i]] = 1
            else:
                mapper1[s[i]] += 1
            if t[i] not in mapper2:
                mapper2[t[i]] = 1
            else:
                mapper2[t[i]] += 1
            i += 1
        
        return mapper1 == mapper2