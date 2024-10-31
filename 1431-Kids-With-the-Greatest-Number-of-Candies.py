class Solution:
    #returns greatest number in array
    def greatestNum(self, array: List[int]) -> int:
        greatest = 0
        for i in range(0, len(array)):
            if array[i] > greatest: greatest = array[i]
        return greatest

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = self.greatestNum(candies)
        result = []
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result

