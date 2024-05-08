test1 = """{}"""

def isValidParent(testString):
    stack = []
    for char in testString:
        if char =='{' or char =='[' or char =='(': #append these char using empty list 
            stack.append(char)
        else:
            if not stack: #check if stack is empty 
                return False
            if (char == '}' and stack[-1] != '{') or (char == ']' and stack[-1] != '[') or (char == '(' and stack[-1] != ')'): # check the opposite case, if one of case not matched return false directly
                return False
            stack.pop() 
    return not stack #true only the stack is empty at the end 

print(isValidParent(test1))

