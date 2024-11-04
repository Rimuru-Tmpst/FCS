#Exercise 1.Use a stack or a queue (or both!) to determine if a given input is a palindrome or not.

from collections import deque

def is_palindrome_stack_queue(word):
    stack = []
    queue = deque()
    for char in word.lower():  
        stack.append(char)
        queue.append(char)
    while stack:
        if stack.pop() != queue.popleft():
            return False
    return True

print(is_palindrome_stack_queue("mom"))           
print(is_palindrome_stack_queue("Neveroddoreven"))  
