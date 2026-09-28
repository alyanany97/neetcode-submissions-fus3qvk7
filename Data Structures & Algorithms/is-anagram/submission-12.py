class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        scount = defaultdict(int)
        tcount = defaultdict(int)

        for letter in range(len(s)):
            scount[s[letter]] += 1
            tcount[t[letter]] += 1
        
        if scount == tcount:
            return True
        else:
            return False


        