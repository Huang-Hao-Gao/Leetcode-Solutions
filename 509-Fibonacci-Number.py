class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        former = 0
        latter = 1
        current = 0
        for _ in range(2, n + 1):
            current = former + latter
            former = copy.copy(latter)
            latter = copy.copy(current)
        print(current)
        return current