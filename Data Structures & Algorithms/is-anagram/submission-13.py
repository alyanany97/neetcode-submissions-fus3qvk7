from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = defaultdict(int) #any keys value starts at 0
        t_count = defaultdict(int)

        for char in s:
            s_count[char] += 1
        
        for char in t:
            t_count[char] += 1
        
        if s_count == t_count:
            return True
        
        return False

