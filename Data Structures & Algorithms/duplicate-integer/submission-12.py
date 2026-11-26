class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False

#O(n) time and O(n) space more memory for more speed compared to brute force. 
#O(n) space because seen can grow to n values within it!
            
        