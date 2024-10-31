class Solution:
    def reverseString(self, s: List[str]) -> None:
        \\\
        Do not return anything, modify s in-place instead.
        \\\
        #create a loop which moves a character to the front of the array
        i = 1
        while i < len(s):
            s.insert(0, s.pop(i))
            i+=1
        

        