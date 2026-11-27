import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        heap = []

        for num, freq in count.items(): #loop over the unique keys
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for freq, num in heap:
            res.append(num)
        
        return res
        
        

