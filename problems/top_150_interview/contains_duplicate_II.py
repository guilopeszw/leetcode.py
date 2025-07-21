class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        between = {}
        for i in range(len(nums)):
            if nums[i] in between and i - between[nums[i]] <= k:
                return True
            between[nums[i]] = i
        return False