from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h : the number of hours you have to eat all the bananas
        # k : the bananas-per-hour eating rate
        # If h >= len(piles), then we can eat all bananas within \
        # len(pile) hours by chooing k = max(piles)
        # k = [1,max[pile])
        # Binary search the minimum k s.t total time <= h

        min_k = 0
        start, end = 1, max(piles)

        while start <= end:
            mid = start + (end-start)//2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/mid)
                
            if hours <= h:
                min_k = mid
                end = mid-1
            elif hours > h:
                start = mid+1

        return min_k



