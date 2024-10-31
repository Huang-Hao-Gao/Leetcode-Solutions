class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #use 1st and last coordinate to form a straight line, then check 
        #if every coordinate between the 1st and last coordinate lie on the line

        #find gradient of line
        maxY = coordinates[len(coordinates)-1][1]
        minY = coordinates[0][1]
        maxX = coordinates[len(coordinates)-1][0]
        minX = coordinates[0][0]
        try:
            m = (maxY-minY) / (maxX-minX)

         #change in x = 0, check if the x value of all coordinates are the same
        except ZeroDivisionError:
            for i in range(1, len(coordinates) - 1):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True 


        #change in y = 0, check if y value of coords are the same
        if m==0:
            for i in range(1, len(coordinates) - 1):
                if coordinates[i][1] != coordinates[0][1]:
                    return False
            return True 


        #at this point m !=0
        #find intercept
        c = maxY - m*maxX
        
        for i in range(1, len(coordinates) - 1):
            if coordinates[i][1] != m*coordinates[i][0] + c:
                return False

        return True 