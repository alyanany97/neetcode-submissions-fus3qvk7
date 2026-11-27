class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = defaultdict(int)

        for i, num in enumerate(nums):
            
            difference = target - num
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i
            
        return []
        
#O(n) time and O(n) space because the seen memory can grow with n
