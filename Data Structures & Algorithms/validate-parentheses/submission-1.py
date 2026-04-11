class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            print(stack)
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                item = stack.pop() if stack else None
                print(item, char)
                if (item != '(' and char == ')') or (item != '{' and char == '}') or (item != '[' and char == ']'):
                    return False 
        print(len(stack))
        if len(stack) == 0:
            return True
        return False
        