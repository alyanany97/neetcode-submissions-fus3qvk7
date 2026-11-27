from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)
            anagram[sorted_word].append(word)

        return list(anagram.values())

#O(n * nlogn) because of the sorting per string and O(n) because sorted creates a new list