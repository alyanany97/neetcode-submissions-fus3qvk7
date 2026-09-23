class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for i in range(len(s)):
            hashmap_s[s[i]] += 1
            hashmap_t[t[i]] += 1
        if hashmap_s == hashmap_t:
            return True
        
        return False