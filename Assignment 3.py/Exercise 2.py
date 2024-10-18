#Exercise 2 Given a list of characters and an integer n, generate, using recursion, all possible combinations of length n that contain the characters in the list.


def generate_combinations(characters, n, current_combination=""):
    if len(current_combination) == n:
        print(current_combination)
        return
    
    for char in characters:
        generate_combinations(characters, n, current_combination / char)