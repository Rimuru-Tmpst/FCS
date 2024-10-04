# 2. Write a program that repeatedly asks the user for a letter, and then prints all the names in this list that contain the letter.

names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

while True:
    letter = input("Enter a letter (or 'exit' to quit): ").strip().lower()

    if letter == 'exit':
        break

    found = False
    for name in names:
        if letter in name.lower():
            print(name)
            found = True
            
    if not found:
        print(f"No names contain the letter '{letter}'.")