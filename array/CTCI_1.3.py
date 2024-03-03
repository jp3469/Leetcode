''' 
Given two strings, write a method to decide if one is a permutation of the other.

1. Describe the question
Given two strings, determine if one string is the same as the other string but just rearranged.
2. What are the constraints

3. What are some examples given, and can you solve it by hand?
'abcd' 'dbca' => True
'aaa' 'aa' => False
'' '' => True
'aa' 'aa' => True
'?abv12' 'a1b?2c' => True
4. Any other insights you find
it is a permutation if it contains the same characters and the same number of those characters and nothing else

create a dictionary
for each character in s1:
    if character in dictionary:
        dictionary value += 1
    else:
        add to dictionary and set value to 1

do the same for s2

if dict1 == dict2 return true
else return false

'''

def permut(s1, s2):
    dict1, dict2 = {}, {}
    for char in s1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    
    for char in s2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1
    
    if dict1 == dict2:
        return True
    return False

s1 = 'abcd'
s2 = 'dbca'
s3 = 'aaa'
s4 = 'aa'
s5 = ''
s6 = '?abc12'
s7 = 'a1b?2c'

print(permut(s1, s2))
print(permut(s3, s4))
print(permut(s5, s5))
print(permut(s4, s4))
print(permut(s6, s7))

'''runtime is O(n) since you are just looping through the strings once and the runtime for comparing dictionaries is also O(n) meaning the total runtime would be O(2n)
space complexity is O(n) since you are creating a dictionary with each item being a character in the string. 
can optimize by exiting early if not equal
'''