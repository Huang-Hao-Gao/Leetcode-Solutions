#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(1, len(nums) - i):
                if(nums[i] + nums[i + k] == target):
                    return [i, i + k]
# @lc code=end

