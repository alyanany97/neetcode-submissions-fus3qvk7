class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        maxLength = 0
        counts = {}

        left = 0
        right = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxFreq = max(maxFreq, counts[s[right]])

            while (right - left + 1) - maxFreq > k:
                counts[s[left]] -= 1
                left +=1
            
            maxLength = max(maxLength, right - left + 1)
            
        return maxLength

