class Solution:
    def isValid(self, s: str) -> bool:
        openToClosed = {
            '(':')',
            '[':']',
            '{':'}'
        }
        open = ['(', '[', '{']
        closed = [')', ']', '}']

        #if the size of the string is odd, return False since it can't be valid
        #define a stack 
        #if I have an open bracket, push it onto the stack
        #if I have a closed bracket, check if it matches the last element on the stack
            #if the stack is empty, return False
        #if it matches, pop the open bracket off the stack and move onto the next element
        #by the time I reach the end, the stack should be empty, then return true
        if len(s) % 2 == 1: return False
        stack = []
        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            else:
                #closed bracket
                if len(stack) == 0: return False
                if openToClosed[stack[-1]] != s[i]: return False
                stack.pop()
        return not len(stack) != 0
