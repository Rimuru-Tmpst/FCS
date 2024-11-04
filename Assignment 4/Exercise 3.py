def decode_message(message):
    stack = []
    for char in message:
        if char.isalpha() or char == ' ':  
            stack.append(char)
        elif char == '*':  
            if stack:
                stack.pop()

    
    decoded_message = ''.join(reversed(stack))
    return decoded_message

# Test case
decoded = decode_message(" ****** DAED TNSI   *** SIVLE")
print(decoded)  
