'''
Write a method to replace all spaces in a string with '%20'.

1. Describe the question
Replace all spaces in a string with the string '%20'
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
"Mr John Smith" => "Mr%20John%20Smith"
"   " => "%20%20%20"
"" => ""
"Hello" => "Hello"
4. Any other insights you find

turn the string into an array
for char in array:
    if char == ' ':
        char = '%20'
return ''.join(arr)

'''

def replace(s):
    string = list(s)
    for index, char in enumerate(string):
        if char == ' ':
            string[index] = '%20'
    return ''.join(string)

s1 = "Mr John Smith"
s2 = "   "
s3 = ""
s4 = "Hello"

print(replace(s1))
print(replace(s2))
print(replace(s3))
print(replace(s4))

'''runtime is O(n) since we are looping through the string
space complexity is O(n) since we are turning the string into an array
runtime can't be optimized since we need to loop through the string
maybe space complexity can be optimized by not turning it into an array and doing it in place. not sure how to do this solution is a bit different since in java

'''
