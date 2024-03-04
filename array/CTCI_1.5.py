''' 
Implement a method to perform basic string compression using the counts of repeated characters. 
If the "compressed" string would not become smaller than the original string, your method should return the original string.

1. Describe the question
In a string, if any characters are repeated consecutively, compress the string so that each character is followed by the number of times it appears consecutively in the string. 
If the length of the new string is not smaller than the original string, the original streing should be returned.
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
'aabcccccaaa' => 'a2b1c5a3'
'aabcda' => 'aabcda'
'' => ''
4. Any other insights you find
the character count is only the number of same characters that appear consecutively
it might be easier to convert all of the strings and then determine whether the original string will be shorter

convert the string to an array
make a new array that will get returned
index counter
while index < len(arr):
    set char counter numchar to 1
    while arr[index + 1] != null and arr[index + 1] == arr[index]:
        numchar += 1
    numchararr.append(arr[index])
    numchararr.append(numchar)
    index += numchar
if len(numchararr)>arr:
    return ''.join(arr)
return ''.join(numchararr)

'''

def concatenate(s):
    arr = list(s)
    newarr = []
    index = 0
    while index < len(arr):
        numchar = 1
        curr = arr[index]
        while index+numchar < len(arr) and arr[index + numchar] == curr:
            numchar += 1
        newarr.append(curr)
        newarr.append(str(numchar))
        index += numchar
    if len(newarr)>len(arr):
        return ''.join(arr)
    return ''.join(newarr)

s1 = 'aabcccccaaa'
s2 = 'aabcda'
s3 = ''

print(concatenate(s1))
print(concatenate(s2))
print(concatenate(s3))

'''Runtime is O(n) since we are looping through the original string once.
Space complexity is O(n) since we are creating a new string that is returned. 
'''