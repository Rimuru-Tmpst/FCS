# 3. Given the list: number = [-12, 4, 12, 25, 67], write a program that repeatedly asks the user to input a number, and then insert that number in its correct position in the list. And then print the list. Keep asking the user to input a number until they input the value -99.

numbers = [-12, 4, 12, 25, 67]

while True:
    
    user_input = input("Enter a number to insert (or -99 to quit): ")

    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue 

    if number == -99:
        print("Exiting the program.")
        break 

    numbers.append(number) 
    numbers.sort()         

    print("Updated list:", numbers)

