class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list to a set for O(1) lookups

        numSet = set(nums)
        longest = 0

        for n in numSet:
            #check where to start
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max (longest, length)
        return longest
        
#O(n)