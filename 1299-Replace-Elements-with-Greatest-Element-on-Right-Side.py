class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        curPos = 0
        sortedWithI = []

        def sortByVal(list):
            return list[0]

        for i in range(len(arr)):
            sortedWithI.append([arr[i], i])

        sortedWithI.sort(reverse=True, key=sortByVal)
        print(sortedWithI)
        for i in range(len(arr)):
            if sortedWithI[i][1] - curPos > 0:
                for _ in range(sortedWithI[i][1] - curPos):
                    result.append(sortedWithI[i][0])
                curPos = sortedWithI[i][1] 
        result.append(-1)
        return result