class Solution:
    def isPalindrome(self, s: str) -> bool:
        #turn phrase all into lowercase
        s = s.lower()

        #remove all non-alphanumeric characters
        alnu = list(string.ascii_lowercase) + list(string.digits)
        onlyAlnu = \\
        #if the xth letter of the string is an alphanumeric character, append it to onlyAlnu
        for strIndex in range(len(s)):
            for listIndex in range(len(alnu)):
                if s[strIndex] == alnu[listIndex]:
                    onlyAlnu = onlyAlnu + s[strIndex]     

        #create pointer for 1st and last character of string
        left = 0
        right = len(onlyAlnu) - 1

        #if the pointers cross without any mismatches, then it's a palindrome
        #otherwise it isn't
        while left < right:
            if onlyAlnu[left] != onlyAlnu[right]:
                return False
            left += 1
            right -= 1

        return True