class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = \\
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                try:
                    if strs[0][i] != strs[j][i]:
                        return result
                except:
                    return result
            result += strs[0][i]
        return result
        
            
        