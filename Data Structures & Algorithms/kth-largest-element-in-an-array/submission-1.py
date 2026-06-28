class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums] #O(n)
        heapq.heapify(nums) #O(n)

        while (k-1) > 0: 
            heapq.heappop(nums) #O(klogn)
            k-=1

        return -nums[0]