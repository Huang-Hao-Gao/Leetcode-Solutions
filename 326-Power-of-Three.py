class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 3:
            return n == 3 or n == 1
        
        return self.isPowerOfThree(n / 3)