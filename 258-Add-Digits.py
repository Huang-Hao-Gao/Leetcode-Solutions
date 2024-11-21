class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num

        toStr = str(num)
        sum = 0
        for i in range(len(toStr)):
            sum += int(toStr[i])

        return self.addDigits(sum)
        