class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_indices = {}

        for i, num in enumerate(nums):
            # If number already exists, check distance
            if num in num_indices:
                if i - num_indices[num] <= k:
                    return True
            
            # Update the latest index of the number
            num_indices[num] = i

        return False