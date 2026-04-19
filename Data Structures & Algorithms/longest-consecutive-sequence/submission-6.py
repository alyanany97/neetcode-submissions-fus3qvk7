class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        longestLength = 0

        for num in numSet:
            if(num - 1) not in numSet:
                currentNum = num
                currentLength = 1
            
                while (currentNum + 1) in numSet:
                    currentNum += 1
                    currentLength += 1
            
                longestLength = max(longestLength, currentLength)
        
        return longestLength
            