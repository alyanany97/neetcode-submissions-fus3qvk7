class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            hashmap[sorted_s] = hashmap.get(sorted_s, []) + [s]
        
        return list(hashmap.values())