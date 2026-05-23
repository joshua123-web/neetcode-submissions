class Solution:
    def isValid(self, s: str) -> bool:
        vals = {'(':')', '{':'}', '[':']'}

        n = len(s)

        stack = []

        for i in range(n):
            if s[i] in vals:
                stack.append(s[i])
            else:
                if stack:
                    val = stack.pop()
                    if vals[val] == s[i]:
                        continue
                    else:
                        return False
                else:
                    return False
        
        if stack:
            return False
        return True


       
        
                




            



        