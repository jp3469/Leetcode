# visualize and solve the problem before writing any code
# Use examples to understand the problem and devise strategy.
# With arrays, it's OK to itereate through an array multiple times and transform it to certain
# "states" that's easy to work with. iterating 2-x times is still O(n) as long as you're not doing double for loop.
# For most array questions, the best you can do is O(n) because you need to see each element at least once

# [0,1,2,0,2,1] if my pivot is A[3] = 0 
# [0,0,1,2,2,1,1] # the two zeroes have to appear before everything else because it's equal to 0
# [0,0,2,2,1,1,1] # this is also valid
# a reaonsable order is keeping other elements in the same order that it appeared, relatively.
#  We need to find a way to identify elements, and move them
# 2 subproblems: finding elements that fit our condition, and moving them

# brute force [0,1,2,0,2,1] -> [0,0,1,2,2,1,1] with infinite memeory and time
# sorting does work
# loop through every element, check if it's <, =, or >, use an array that has value or false
# make an array that assigns value, 3 would do here
# less_than = [], equal = [], larger = [].
# sorting them into buckets
# less_than + equal + larger

# Runtime O(n)
# Space O(n) -> O(1)

# initial thought is one array and insert it in order
# return that array. 
# two pointers, find a value that's less than the pivot, insert it at the index of the first pointer. move that pointer up by 1
# if you find a value that's equal to the pivot, keep track of count
# if you find a value that's greater than the pivot, insert at the end or the index of the second pointer, move that pointer down by 1
# at the end, add back the number of elements equal to the pivot. use a for loop

def sort_array_2(arr, pivot_index):
    # initilize a new array
    new_arr = [0]*len(arr)
    pivot = arr[pivot_index] # arr[3] = 0
    beginning_pointer = 0
    end_pointer = len(arr) - 1
    count = 0 

    for x in arr:
        if x < pivot:
            new_arr[beginning_pointer] = x
            beginning_pointer += 1
        elif x == pivot:
            count += 1
        else:
            new_arr[end_pointer] = x
            end_pointer -= 1

    for y in range(count):
        new_arr[beginning_pointer] = pivot
        beginning_pointer += 1

    return new_arr 

def sort_array(arr, pivot_index):
    lt, equal, larger = [], [], [] # this needs to go away
    # lt = []
    # equal = [0,0]
    # larger = [1,2,2,1]
    pivot = arr[pivot_index] # arr[3] = 0

    for x in arr: # [0,1,2,0,2,1] 
        if x < pivot:
            lt.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return lt + equal + larger # [0,0,1,2,2,1]

def sort_array_3(arr, pivot_index):
    pivot = arr[pivot_index]

    lt = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    return lt + equal + larger

print(sort_array([0,1,2,0,2,1], 3))
print(sort_array_2([0,1,2,0,1,2], 3))
print(sort_array_3([0,1,2,0,2,1], 3))
# print(sort_array([], 3))