
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        left = 0
        res = 0

        for right, char in enumerate(s):
            count[char] += 1 
            changesNeeded = (right - left + 1) - max(count.values())
            
            while changesNeeded > k:
                count[s[left]] -= 1
                left += 1
                changesNeeded = (right - left + 1) - max(count.values())
            
            res = max(res, right - left + 1)
        
        return res
                






        
