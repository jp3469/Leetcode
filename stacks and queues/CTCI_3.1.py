'''
Describe how you could use a single array to implement three stacks

Approach 1: Fixed Division
- We can divide the array in three equal parts and allow the individual stack to grow in that limited space
- ex: for stack 1, we will use [0, n/3), for stack 2, we will use [n/3, 2n/3), for stack 3, we will use [2n/3, n).
- the problem with this approach is that one stack might run out of space while the others are nearly empty
- one way to accommodate this problem is by having some kind of algorithm that better allocates space so we can minimize this problem.

Approach 2: Flexible Division
- When one stack exceeds its initial capacity, we grow the allowable capacity and shift elements as necessary. 
- fixes the problem of running out of space, but is very hard to implement. 
'''