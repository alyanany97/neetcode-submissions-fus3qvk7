class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        maxLength = 0

        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1)
            
            seen[char] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength



