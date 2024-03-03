# [1,2,9] -> [1,3,0]
# [9] -> [1,0]

# my initial attempt
def increment(arr):
    last_element = arr[-1]
    if last_element < 9:
        arr[-1] += 1
        return arr
    if len(arr) == 1:
        arr.append(0)
        arr[0] = 1
        return arr
    else:
        new_arr = increment(arr[:-1])
        return new_arr + [0]
# time complexity = O(n)
# space complexity = O(n)

# answer: brute force would be to convert the elements of the array into an integer and add one and then put it back into array form
# solution used for loop instead of recursion and did not create any new arrays
def increment_2(arr):
    arr[-1] += 1
    for index in range(1, len(arr)):
    # need to stop at index 1 because if index 0 needs to be changed, it'll be changed by the previous loop, otherwise index will be out of range
        if arr[-index] != 10:
            break
        arr[-index] = 0
        arr[-index - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr
# time complexity = O(n)
# space complexity = O(1)

print(increment([1,2,9]))
print(increment([9]))
print(increment([9,9,9,9]))
print(increment_2([1,2,9]))
print(increment_2([9]))
print(increment_2([9,9,9,9]))

# Variant: Write a program which takes as input two strings s and t of bits encodingbinary numbers B1, and 
# B2, respectively, and refurns a new string of bits representing the number B1 + B2.