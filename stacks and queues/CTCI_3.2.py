'''
How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element?
Push, pop, and min should all operate in O(1) time.

We could do this by having one space in the array allocated for the minimum of the array.
This would mean that any time an element is added to the array, we would first need to check if that element is smaller than the minimum of the array,
and replace the minimum if it is. 

There is a problem with my above solution. When the minimum is popped from the stack, the minimum would have to revert back to the original minimum.
This problem can be solved by keeping track of the minimum at each "state" of the stack. 
This means that whatever the minimum of the array is at the time when a certain element is at the top of the stack, should be recorded in order to keep track of the minimum at that state.,.

'''