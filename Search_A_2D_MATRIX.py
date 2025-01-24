from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n-1
        while start <= end:
            mid = start + (end-start)//2
            mid_m = mid // n
            mid_n = mid % n
            if matrix[mid_m][mid_n] == target:
                return True
            elif matrix[mid_m][mid_n] > target:
                end = mid-1
            elif matrix[mid_m][mid_n] < target:
                start = mid+1
        return False

