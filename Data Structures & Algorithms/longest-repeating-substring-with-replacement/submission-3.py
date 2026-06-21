class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
        
        left = 0
        most_fr = 0
        count = [0] * 26
        final = 0 
        
        for right in range(len(s)):

            idx = ord(s[right]) - ord('A')
            
            count[idx] += 1 
           
            most_fr = max(most_fr, count[idx]) # keeping track of most freq elements
            
            window_size = right - left + 1

            if window_size - most_fr <= k:

                final = max(window_size, final)
            else:
                
                while window_size - most_fr > k and left < len(s):
                    idx2 = ord(s[left]) - ord('A')
                    count[idx2] -= 1
                    left += 1
                    window_size = right - left + 1
            
            final = max(window_size, final)

        
        return final

                        



            
            


