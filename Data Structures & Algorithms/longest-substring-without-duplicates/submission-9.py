class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        maxCount = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            maxCount = max(maxCount, right - left + 1)

        return maxCount
            

#Shrink while invalid
#after while ADD to window
#Record AFTER the while
#Time = O(n)
#Space = O(n) if any character is possible, O(1) if only 26 letters
            
            
        
        
                    
            
