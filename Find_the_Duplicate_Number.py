from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        for num in nums:
            if num not in hashmap:
                hashmap[num].append(num)
            else:
                return num
        return -1