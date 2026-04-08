class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # create a dictionary for fast lookup. 
        for i, num in enumerate(nums): # i = index, num = value at that index
            need = target - num
            if need in seen:
                return [seen[need], i] # seen[need] = index of the number we saw earlier thats needed, go into the dictionary and find the key need and return me its value(index)
                                        # i, is the current index of the number we are on in the list.
            seen[num] = i; #put the number in the dictionary and its value as its index i. 

        
