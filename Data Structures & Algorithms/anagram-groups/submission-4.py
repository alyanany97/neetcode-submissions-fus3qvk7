from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            hashmap[sorted_s].append(s) #we can do this without initializing hashmap[sorted_s] because of defaultdict(list) 
                                        # which automatically created it with value []

            
            
        return list(hashmap.values())
