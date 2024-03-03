'''' 
Implement a function to reverse a string

1. Describe the question
taking a string and reversing it
2. What are the constraints
string length is between 0 and 1000
3. What are some examples given, and can you solve it by hand?
'abcd' => 'dcba'
'aaba' => 'abaa'
'' => ''
4. Any other insights you find
No

find length of string
create an array of the same length
for character in string:
    array[length - 1] = character
    length -= 1
return ''.join(array)
'''

def reversal(s):
    length = len(s)
    arr = [''] * length
    for char in s:
        arr[length - 1] = char
        length -= 1
    return ''.join(arr)

s1 = 'abcd'
s2 = 'aaba'
s3 = ''

print(reversal(s1))
print(reversal(s2))
print(reversal(s3))

'''runtime is O(n) because we are looping through the string
space complexity is O(n) because we are creating an array of size n
can't optimize runtime since we have to loop through the string but can optimize space complexity by swapping instead of creating an array
'''

'''
find length of string divide by 2
for length of string divide by 2:
    array[i], array[(i+1) * -1]] = array[(i+1) * -1], array[i]
return string
'''

def reversal2(string):
    s = list(string)
    for i in range(len(s)//2):
        s[i], s[(i+1) * -1] = s[(i+1) * -1], s[i]
    return ''.join(s)

print(reversal2(s1))
print(reversal2(s2))
print(reversal2(s3))