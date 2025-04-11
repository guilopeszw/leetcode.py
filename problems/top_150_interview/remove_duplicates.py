class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        while k < len(nums):
            if nums[k] == nums[k - 1] and len(nums) != 1: 
                nums.pop(k - 1)
            else:
                k += 1
        return k