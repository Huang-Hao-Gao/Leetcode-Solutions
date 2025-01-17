class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return n == 1
        numPlants = 0
        numZeros = 0
        foundOne = False
        for i in range(len(flowerbed)):
            if i == (len(flowerbed) - 1) and flowerbed[i] == 0:
                numZeros += 1
                numPlants += numZeros // 2
                if not foundOne and len(flowerbed) % 2 == 1: #not foundOne means the whole list is 0
                    numPlants += 1
                if numPlants >= n:
                        return True

            elif flowerbed[i] == 0:
                numZeros += 1
            else: #it's a 1
                if not foundOne and numZeros >= 2:
                    numPlants += numZeros // 2
                    foundOne = True
                    numZeros = 0
                    if numPlants >= n:
                        return True
                
                elif numZeros > 2:
                    if numZeros % 2 == 1:
                        numPlants += numZeros // 2
                    else:
                        numPlants += numZeros / 2 - 1
                    if numPlants >= n:
                        return True
                if not foundOne:
                    foundOne = True
                numZeros = 0
        return False