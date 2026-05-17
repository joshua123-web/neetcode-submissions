class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vals1 = {}
        vals2 = {}

        i = 0
        j = 0

        while i < len(s):
            if s[i] not in vals1:
                vals1[s[i]] = 1
            else:
                vals1[s[i]] += 1
            i += 1
        
        while j < len(t):
            if t[j] not in vals2:
                vals2[t[j]] = 1
            else:
                vals2[t[j]] += 1
            j += 1
        
        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))

        k = 0

        return vals1 == vals2