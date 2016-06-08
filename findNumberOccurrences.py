""" 
Find number of occurrences of x in a sorted array
Input: a sorted array and an integer x 
Ouput: How many times x occour in the array 
"""

def bsearch(arr, x, first):
"""
    arr: integer array 
    x: integer 
    first: boolean to check if we look for first or last occurrence of x
"""

    start = 0
    end = len(arr)-1
    result = -1

    while (start <= end):
        mid = (start+end)/2
        if arr[mid] == x:
            result = mid
            if first:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return result

myArr = [1,2,3,42,42,42,71,100]
first = bsearch(myArr, 42, True)
last = bsearch(myArr, 42, False)

print last - first + 1


