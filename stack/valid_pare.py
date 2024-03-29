test1 = """{}"""

def isValidParent(testString):
    stack = []
    for char in testString:
        if char =='{' or char =='[' or char =='(':
            stack.append(char)
        else:
            if not stack:
                return False
            if (char == '}' and stack[-1] != '{') or (char == ']' and stack[-1] != '[') or (char == '(' and stack[-1] != ')'):
                return False
            stack.pop()
    return not stack

print(isValidParent(test1))

