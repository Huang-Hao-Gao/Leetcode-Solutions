class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            lessThan = 0
            for j in range(len(nums)):
                if j == i: continue
                if nums[j] < nums[i]:
                    lessThan +=1
            result.append(lessThan)
        return result