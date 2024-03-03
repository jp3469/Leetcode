''' Implement an algorithm to determine if a string has all unique characters. What if we can't use additional data structures?

Constraints - characters are lowercase alphabetical characters only

Examples - 
    'abcd' True
    'abda' False

Questions -
    How long is the string? 1000 characters
    There are 26 unique lowercase alphabetical characters
    There are 52 unique alphabetical characters (lowercase and uppercase)

  
For the characters in the string
    if character exists in list
        return false
    if character doesn't exist in list
        add to list
        go to next character
    return true
'''

def unique(string):
    array = []
    for char in string:
        if char in array:
            return False
        else:
            array.append(char)
    return True

string1 = 'abcd'
string2 = 'abda'

print(unique(string1))
print(unique(string2))

''' runtime = O(1) because the alphabet only has 26 characters'''

''' if we use a hashtable the lookup time is O(1) instead of O(n) for an array'''

def unique(string):
    hashtable = {}
    for char in string:
        if char in hashtable:
            return False
        else:
            hashtable[char] = True
    return True


def unique(string):
    array = [False] * 26
    for char in string:
        num = lettertonumber(char)
        if array[num]:
            return False
        else:
            array[num] = True
    return True

def lettertonumber(char):
    return ord(char) - 97

