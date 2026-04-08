class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #If two strings have different lengths, they can NEVER be anagrams
        #EARLY EXIT --> works without it, just good to increase efficiency. 
        if len(s) != len(t):
            return False
        
        count = {} #Create a dictionary to store the key:value pair --> 'Letter" : count
        for char in s: #first time we see its character start its count at 1, Every time after that increment its count
            if char in count:
                count[char] += 1
            else:
                count[char] = 1 # MUST create the key:value pair first this way. AND THEN we can do +=1

        for char in t: #for every character in string t, if its not in the count populated by iterating through string s, then return false right away. If it is just subtract the count by 1 to bc rememeber, the counts of each letter needs to match. so if after iterating through string s we have 'a' appearing 4 times. and we get to an 'a' in string t just subtract the count of key 'a' to make it 3 now. Now we need to see a 3 more times!
            if char not in count:
                return False
            else:
                count[char] -=1 # goal is to get count back to 0
            
            if count[char] < 0: # This means theres more of this character in string t, than what was counted in string s
                return False

        return True


        
        