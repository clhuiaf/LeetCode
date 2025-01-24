from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r: 
            temp_area = min(heights[l],heights[r])*(r-l)
            if temp_area > max_area:
                max_area = temp_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area