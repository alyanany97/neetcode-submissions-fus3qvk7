class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        right = 0
        maxCount = 0

        for left in range(len(s)):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
            
            maxCount = max(maxCount, right - left)
            
            seen.remove(s[left])

        return maxCount
            

                
            
            
        
        
                    
            
