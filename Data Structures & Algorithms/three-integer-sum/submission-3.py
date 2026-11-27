class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        seen = set()
        res = []
        
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    


            seen.add(nums[i])
        
        return res


#Time = O(n2)
#Space = O(n)
#Really do need to check for duplicates for i and for the loop within for left

