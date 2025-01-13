class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums[1:])
        for i in range(len(nums)):
            if leftSum == rightSum:
                return i
            if i == len(nums) - 1: return -1
            leftSum += nums[i]
            rightSum -= nums[i+1]
        