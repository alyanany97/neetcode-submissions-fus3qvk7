class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLength = 0

        left = 0
        right = 0

        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1)

            seen[char] = right
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
