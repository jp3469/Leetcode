'''
Write a program to sort a stack in ascending order (with biggest items on top). 
You may use at most one additional stack to hold items, but you may not copyu the elements into any other data structure (such as an array).
The stack supports the following operations: push, pop, peek, and isEmpty

1. Describe the question
given a stack, sort it so that the biggest items are at the top
2. What are the constraints
May only use one additional stack to hold items
3. What are some examples given, and can you solve it by hand?
[1,3,5,2,6,7,2,3,4] => [1,2,2,3,3,4,5,6,7]
4. Any other insights you find

'''
import stack

def sort_stack(s):
		r = stack.Stack()
		while not s.isEmpty():			
			tmp = s.pop()
			while not r.isEmpty() and r.peek() > tmp:
				s.push(r.pop())
			r.push(tmp)
			while not s.isEmpty() and s.peek() >= r.peek():
				#warning, >= here
				r.push(s.pop())
		return r

s = stack.Stack()
s.push(1)
s.push(3)
s.push(5)
s.push(2)
s.push(6)
s.push(7)
s.push(2)
s.push(3)
s.push(4)

print(sort_stack(s))

'''runtime is O(N) since we are looping through the stack 1 time.
space complexity is O(N) since we are creating one new stack to hold values.'''