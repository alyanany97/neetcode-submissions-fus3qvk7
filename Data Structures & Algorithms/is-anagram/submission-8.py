class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_count = {}
        s_count = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        return s_count == t_count

