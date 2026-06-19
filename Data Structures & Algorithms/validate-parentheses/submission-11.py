class Solution:
    def isValid(self, s: str) -> bool:
        
        vals = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for i in s:
            if i in vals:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                j = stack.pop()
                    
                if vals[j] != i:
                    return False
        
        if stack:
            return False
        return True
        
       

           


       
        
                




            



        