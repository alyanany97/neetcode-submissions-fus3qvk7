import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        #duplicates dont matter
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])

            while len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

    
        

