class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        maxFreq = 0
        maxLength = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            maxFreq = max(maxFreq, counts[char])

            
            while (right - left + 1) - maxFreq > k:
                counts[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength


