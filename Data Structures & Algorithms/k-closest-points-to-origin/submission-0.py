class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #[[0,1],[1,0]]
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist,x,y]) #put all numbers in minHeap

        heapq.heapify(minHeap) #heapify it
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1 

        return res