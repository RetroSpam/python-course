def bracket_balance(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

print(bracket_balance("()"))
print(bracket_balance("[(])"))
print(bracket_balance("{[()]}"))
print(bracket_balance("}"))
print(bracket_balance("[]["))
print(bracket_balance(")("))