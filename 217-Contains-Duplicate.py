class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        #for loop which first checks if a key of the same integer exists, then return true
        #else, create a new key value pair in dictionary with value 1? value doesn't matter right?


        for num in nums:
            if num in dict:
                return True
            #add the integer as a key in the dictionary with an arbitrary value 0
            dict[num] = 0
            
        #if it never returned true, then it must be false
        return False