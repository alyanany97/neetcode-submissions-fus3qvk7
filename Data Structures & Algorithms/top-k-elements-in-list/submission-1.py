import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        hashmap = []

        for num, freq in count.items():
            heapq.heappush(hashmap, (freq, num))
            if len(hashmap) > k:
                heapq.heappop(hashmap) 
            
        return list(num for freq, num in hashmap)