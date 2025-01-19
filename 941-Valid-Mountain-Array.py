class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False
         
        increasing = True
        
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            if increasing:
                if arr[i] > arr[i + 1]:
                    increasing = False
            else:
                if arr[i] < arr[i + 1]:
                    return False

        if increasing:
            return False
        return True