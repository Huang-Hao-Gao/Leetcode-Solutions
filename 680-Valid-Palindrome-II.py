class Solution:

    def palindromeHelper(self, s, i, j):
        s = s[i:j+1]
        length = len(s)
        i = 0
        j = length - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        i = 0
        j = length - 1
        while i < j:
            if s[i] != s[j]:
                return self.palindromeHelper(s, i + 1, j) or self.palindromeHelper(s, i, j - 1)
            i += 1
            j -= 1
        return True