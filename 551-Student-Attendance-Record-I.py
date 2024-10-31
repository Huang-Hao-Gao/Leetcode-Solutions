class Solution:
    def checkRecord(self, s: str) -> bool:
        absentAcc = 0
        lateAcc = 0
        for x in s:
            if x == 'A':
                absentAcc += 1
                lateAcc = 0
                if absentAcc == 2: 
                    return False
            elif x == 'L':
                lateAcc += 1
                if lateAcc == 3:
                    return False
            else:
                lateAcc = 0

        return True

        