class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if num - 1 not in numSet:
                currentLength = 1

                while num + 1 in numSet:
                    num += 1
                    currentLength +=1
                maxLength = max(maxLength, currentLength)
        
        return maxLength

            