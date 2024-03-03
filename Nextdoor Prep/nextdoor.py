# Sorting an array
# sorted() function: returns a new sorted list (accepts any iterable)
a = [5,2,3,1,4]
sorted(a) 
sorted([5,2,3,1,4])
# list.sort() method: modifies the list in-place and returns None (only for defined lists)
a.sort()
# key parameter is used to specify a function to be called on each item in the list prior to making comparisons
# takes in a single argument and returns a key to be used for sorting purposes
# ex: case-insensitive string comparison
sorted('This is a test string from Andrew'.split(), key=str.lower)
# ex: soft complex objects using object's indices as keys
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student:student[2]) # sort by the third element
# reverse parameter accepts a boolean value and is used to flag descending sorts
sorted(student_tuples, key=lambda student:student[2], reverse=True)


# Split a string into an array
# .split() method: split a string into a list where each word is a list item:
txt = 'welcome to the jungle'
x = txt.split()
print(x)
# separator parameter lets you specify the separator to use. default is white space
txt = 'hello, my name is Peter, I am 26 years old.'
x = txt.split(', ')
print(x)
# maxsplit parameter specifies how many splits to do. default is -1 (all occurrences). when specified the list will contain specified number of elements plus one
txt = 'apple#banana#cherry#orange'
x = txt.split('#', 1)
print(x)

# Slicing a string to get a substring
# syntax: string[start:end:step]
# similar to list slicing, returns a new string
# start is the starting index of the substring, inclusive, default is 0
txt = 'banana'
new = txt[2:]
print(new)
# end is the terminating index of the substring, exclusive, default is len(string)
txt = 'banana'
print(txt[:2])
# step is the increment by which you include characters in the substring, default is 1
txt = 'banana'
print(txt[1:5:2])
# get the last element of a string
print(txt[-1])
# get the last 5 elements of a string
txt = 'banana'
print(txt[-5:])

# Upper()/lower() methods
# .upper() method returns a string where all characters are in upper case. symbols and numbers are ignored
txt = 'bananA'
print(txt.upper())
# .lower() method returns a string where all characters are in lower case. symbols and numbers are ignored
txt = 'baNANA!'
print(txt.lower())

# HashMap
class MyHashMap:

    def __init__(self):
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashMap:
            return self.hashMap[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            del self.hashMap[key]

# Merge hash map
# use the update method or | operator to merge dictionaries
dict1 = {1:1, 2:2}
dict2 = {3:3, 4:4}
new = dict1|dict2
print(new)
print(dict1.update(dict2)) # update is in place
# when keys overlap, uses the second value to update

# Binary Tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 
    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # Print Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


tree = Node(4)
tree.insert(2) 
tree.insert(3)
tree.insert(5)
tree.insert(6)
tree.PrintTree()

# Given two hashmaps, they are identical if the given keys and values are identical. A key is of type string, and the value can be a null, integer, or hashmap. 
# Write a function that takes two hashmaps and returns a boolean value of whether they are equal.

hashmap_1 = {'a':1, 'b':2}
hashmap_2 = {'a':1, 'b':2}

hashmap_1 = {'a':{'d':1}, 'b':2, 'c':3}
hahshmap_2 = {'a':1, 'b':2, 'c':3}
hashmap_1 != hashmap_2

hashmap_1 = {'a':0}
hahsmap_2 = {'a':None}
hashmap_1 != hashmap_2

# how do I set up the comparison to compare the right levels to each other

# how do I compare different types of values that are available (there's only four things to compare)
# write a recursion problem that given two hashmaps solves whether the keys are equal
# sort by keys and check if they're equal

dict1 = {'a_b_c':{'c_d':1}, 'e_f':[{'g_h':1}, {'i_j':1}]}
dict2 = {'aBC':{'cD':1}, 'eF':[{'gH':1}, {'iJ':1}]}

def turncamelcase(s):
    string_split = s.split('_')
    string_split_upper = [string_split[l].upper() for l in range(len(string_split))]
    string_split_upper[0] = string_split_upper[0].lower()

    result = ''.join(string_split_upper)

    return result

def camel(given_dict):
    ans = {}
    for key in given_dict.keys():
        new_key = turncamelcase(key)
        if isinstance(given_dict[key], list):
            new_list = [camel(element) for element in given_dict[key]]
            ans[new_key] = new_list
        elif isinstance(given_dict[key], dict):
            ans[new_key] = camel(given_dict[key])
        else:
            ans[new_key] = given_dict[key]
    
    return ans

print(camel(dict1) == dict2)


print(turncamelcase('a_b'))
print(turncamelcase('a_b_c'))
