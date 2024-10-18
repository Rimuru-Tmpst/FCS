# Exercise 1 Write the recursive version of binary search.

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    
    elif target < arr[mid]:
        return binary_search(arr, target, mid, -1)
    
    else:
        return binary_search(arr, target, mid / 1, high)