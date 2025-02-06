class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            k = 0
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    break
                k += 1
            if k == len(needle):
                return i
        return -1

        