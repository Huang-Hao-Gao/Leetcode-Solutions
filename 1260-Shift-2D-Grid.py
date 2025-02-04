class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #extract elements into one 1D array row by row
        flatArr = []
        for row in grid:
            for elem in row:
                flatArr.append(elem)
        
        for _ in range(k):
            lastElem = flatArr.pop()
            flatArr.insert(0, lastElem)  
        
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = flatArr[a]
                a += 1
        return grid

        