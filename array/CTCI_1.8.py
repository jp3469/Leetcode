'''
Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 
is a rotation of s1 using only one call to isSubstring.

1. Describe the question
The method isSubstring checks if one word is a substring of another. A substring is a contiguous sequence of characters within a string.
(for example 'the best of' is a substring of 'It was the best of times', but 'Itwastimes' is not.)
We are only allowed to call isSubstring once, and we need to check given two strings if s2 is a rotation of s1. 
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
'waterbottle' 'erbottlewat' => True
'waterbottle' 'erbotltewat' => False
4. Any other insights you find
waterbottle erbottlewaterbottlewat
if s2 is a rotation of s1, if we type out s2 twice consecutively, s1 will be a substring of s2.

s2new = s2+s2
return isSubstring(s2new, s1)

In order to test if this will work, need to write the isSubstring method
Let s1 be the string, and s2 be the substring
if s2 in s1:
    return True
return False
'''


def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False

def isRotation(s1, s2):
    s2new = s2+s2
    return isSubstring(s2new, s1)

s1 = 'waterbottle'
s2 = 'erbottlewat'
s3 = 'erbotltewat'
s4 = 'waterbot'

print(isRotation(s1, s2))
print(isRotation(s1, s3))
print(isRotation(s1, s4))

'''runtime is O(n)(?) since isSubstring checks if s2 is in s1
space complexity is O(n) since we have to create a new string. Maybe this can be optimized by simply calling isSubstring on s2+s2 and s1. 
'''

def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False

def isRotation2(s1, s2):
    return isSubstring(s2+s2, s1)

print(isRotation2(s1, s2))
print(isRotation2(s1, s3))
print(isRotation2(s1, s4))
