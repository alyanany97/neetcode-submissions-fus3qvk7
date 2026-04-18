class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longestStreak = 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                currentNum = num
                currentStreak = 1

                while (currentNum + 1) in numSet:
                    currentNum += 1
                    currentStreak += 1
                
                longestStreak = max(longestStreak, currentStreak)
        
        return longestStreak