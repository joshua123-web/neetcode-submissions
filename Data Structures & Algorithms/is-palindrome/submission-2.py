class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        vals = [ch.lower() for ch in s if ch.isalnum()]


        i = 0

        j = len(vals) - 1

        while i < j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        return True

