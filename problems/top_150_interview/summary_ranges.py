class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, s = 0, 0
        l = []

        while i < len(nums):
            s = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if s != nums[i]:
                l.append(str(s) + '->' + str(nums[i]))
            else:
                l.append(str(s))
            i += 1
        return l