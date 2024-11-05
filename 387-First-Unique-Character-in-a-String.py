class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        #loop through letters in s and add to dict, increasing value by 1 if it already exists
        for l in s:
            if(dict.get(l, 0) == 0):
                dict[l] = 1
            else:
                dict[l] += 1

        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1
    
            