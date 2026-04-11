class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                item = stack.pop() if stack else None
                if (item != '(' and char == ')') or (item != '{' and char == '}') or (item != '[' and char == ']'):
                    return False 
        
        if len(stack) == 0:
            return True
        return False
        