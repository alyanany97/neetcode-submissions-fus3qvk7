class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        minheap = []

        for num, freq in count.items():
            heapq.heappush(minheap, (freq, num))
            if len(minheap) > k:
                heapq.heappop(minheap)

        return list(num for freq, num in minheap)           

