from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()  # Sort the array to simplify logic
        
        for idx, num in enumerate(nums):
            # Skip duplicate values for the current number
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            l, r = idx + 1, len(nums) - 1  
            
            while l < r:
                total = num + nums[l] + nums[r]
                
                if total == 0:
                    triplets.append([num, nums[l], nums[r]])
                    
                    # Skip duplicates for nums[l] and nums[r]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # Move pointers to continue searching
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1  # Increase the left pointer to increase the sum
                else:
                    r -= 1  # Decrease the right pointer to decrease the sum
        
        return triplets