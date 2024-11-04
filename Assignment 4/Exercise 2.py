#Exercise 2.Use a stack or a queue (or both!) to determine if a given expression is balanced.


def is_balanced(expression):
    stack = []
    
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_pairs.values():  
            stack.append(char)
        elif char in bracket_pairs.keys():  
            if not stack or stack.pop() != bracket_pairs[char]:  
                return False

    return len(stack) == 0  

# Test cases
print(is_balanced("(1+2)-3*[41+6]"))     
print(is_balanced("(1+2)-3*[41+6}"))     
print(is_balanced("(1+2)-3*[41+6"))      
print(is_balanced("(1+2)-3*]41+6["))     
print(is_balanced("(1+[2-3]*4{41+6})"))  
