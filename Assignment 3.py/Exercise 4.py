#Exercise 4 : Adding a number to a sorted list


import bisect

def add_to_sorted_list(sorted_list, val):
    
    index = bisect.bisect_left(sorted_list, val)
    
    sorted_list.insert(index, val)


list1 = [1, 34, 56, 78, 89]
val = 77
add_to_sorted_list(list1, val)
print(list1)  
list2 = [1, 3, 56, 234, 789]
val = -99
add_to_sorted_list(list2, val)
print(list2)  
list3 = [1, 3, 56, 234, 789]
val = 789
add_to_sorted_list(list3, val)
print(list3) 
