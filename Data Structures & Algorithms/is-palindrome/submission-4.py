class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        
        if cleaned == cleaned[::-1]:#reversed the string
            return True
        
        return False
             