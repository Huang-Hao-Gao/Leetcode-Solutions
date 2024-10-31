class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'V': 5,
            'I': 1,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        #loop though every letter in string, and add the corresponding number to Result
        x = 0
        while x < len(s) - 1:
            #check if I is before V (IV = 4 not 6)
            if s[x] == \I\ and s[x+1] == \V\:
                result += 4
                x += 2
            elif s[x] == \I\ and s[x+1] == \X\:
                result += 9
                x += 2
            elif s[x] == \X\ and s[x+1] == \L\:
                result += 40
                x += 2
            elif s[x] == \X\ and s[x+1] == \C\:
                result += 90
                x += 2
            elif s[x] == \C\ and s[x+1] == \D\:
                result += 400
                x += 2
            elif s[x] == \C\ and s[x+1] == \M\:
                result += 900
                x += 2
            else:
                result += dict[s[x]]
                x += 1

        
        if x != len(s):
            result += dict[s[len(s)-1]]
        return result