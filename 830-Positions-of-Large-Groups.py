class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        intervals = []
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[start]:
                if i - start >= 3:
                    intervals.append([start, i - 1])
                start = i
        if start < len(s) - 2 and s[-1] == s[start]:
            intervals.append([start, len(s) - 1])
        return intervals