class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #create a hash set to store UNIQUE values only
        
        for num in nums: #iterate through nums
            if num in seen: #if the number is already in our hash set
                return True #return true right away
            seen.add(num) #if it disregards the above if statement, 
                          # that means the number isnt in our hash set, so add it.
        
        return False #if it finishes the above loop and never returns false, 
                     # that means that there are no duplicates!

