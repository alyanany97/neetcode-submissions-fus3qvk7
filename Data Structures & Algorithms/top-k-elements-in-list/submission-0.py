import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        minheap = []

        for num, freq in count.items():
            heapq.heappush(minheap, (freq, num)) #pushes each pair into the minheap, making sure to look at the frequency as the main criteria
                                                 # automatically reordered the list to have the smallest element at index 0 in the min heap list. 
            if len(minheap) > k:
                heapq.heappop(minheap) #pops index 0 (the smallest element/least occuring element in this case)
        
        top_k = list(num for freq, num in minheap) #grab all the numbers from my frequency

        return top_k

