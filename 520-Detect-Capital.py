class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def checkLowerCase(word):
            for i in range(1, len(word)):
                if word[i] == word[i].upper():
                    return False
            return True

        if word[0] != word[0].upper():
            return checkLowerCase(word)
        else:
            if word[1:] == word[1:].upper():
                return True 
            return checkLowerCase(word)

