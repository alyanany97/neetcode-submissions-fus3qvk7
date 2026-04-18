class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in hashmap:
                return list((hashmap[compliment], i))

            hashmap[num] = i