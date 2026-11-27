class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False



#O(nlogn) time bc of the sorting and O(n) because sorted builds a new list that i can join later using "".join(sorted(s))
#cant use sort() because sort changes the string itself and strings cant be changed. use sorted which creates a new string. 