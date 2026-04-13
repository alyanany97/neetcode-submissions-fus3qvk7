class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}


        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen: #compliment is the key because thats what we want to lookup in our hashmap. what we are searching for. 
                return [seen[compliment], i]
            seen[num] = i
        