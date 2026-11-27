class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        count1 = set(nums)
        for num in count1: #make sure to loop over the unique elements
            streak = 0
            curr = num
            if curr - 1 not in count1:
                while curr in count1:
                    streak +=1
                    curr += 1
            
            res = max(res, streak)
        
        return res

#O(n) time and O(n) space
#each number runs in the while loop once because we only start counting at the beginning of a sequence
