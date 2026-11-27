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
            

#for moves the left pointer, while extends the right pointer
#Time = O(n)
#Space = O(n) if any character is possible, O(1) if only 26 letters
            
            
        
        
                    
            
