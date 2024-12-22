from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
    hashmap = {i:[] for i in set(nums)} 

    for i in range(len(nums)):
        hashmap[nums[i]].append(nums[i])

    for j in set(nums):
        if len(hashmap[j]) > 1:
            return True

    return False

        