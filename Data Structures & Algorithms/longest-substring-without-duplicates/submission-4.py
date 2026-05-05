class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLength = 0

        left = 0
        right = 0

        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1) #This is the key here! thats why we need to also enumerate to grab the index so save the characters index and then do plus 1 on that value when we need to shrink the window by moving the left to the old characters value + 1!

            seen[char] = right
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
