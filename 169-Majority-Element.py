class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n % 2 == 0:
            return nums[n // 2 - 1]
        else:
            return nums[n // 2]
                
        