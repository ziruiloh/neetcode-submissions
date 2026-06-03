class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        #height is determined by the shorter line
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max (res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

        # TC = O(n)