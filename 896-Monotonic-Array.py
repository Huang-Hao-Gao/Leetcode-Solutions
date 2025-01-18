class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        i, j = 0, 1
        while nums[i] == nums[j]:
            i += 1
            j += 1
            if j == len(nums):
                return True
        if nums[i] < nums[j]:
            isIncreasing = True
        else:
            isIncreasing = False
        for _ in range(len(nums) - j - 1):
            i += 1
            j += 1
            if isIncreasing and nums[i] > nums[j]:
                return False
            elif not isIncreasing and nums[i] < nums[j]:
                return False
        return True      