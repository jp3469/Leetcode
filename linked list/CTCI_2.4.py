'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.,

1. Describe the question
nodes with values less than x should come before all nodes greater than or equal to x
doesn't matter what order the nodes are in as long as the two sides are partitioned correctly
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
(1,4,5,2,3,None) => (1,2,4,5,3,None)
4. Any other insights you find
    1. we need 4 pointers, one marking the end of the smaller chain, one marking the end of larger chain, one marking the start of larger chain, and one checker. 
    2. find the first smaller and larger incidents and assign the pointers
    3. loop through the rest of the array:
        if smaller: 
            smaller.next = checker
            smaller = smaller.next
        if larger:
            larger.next = checker
            larger = larger.next
        checker = checker.next
    4. set the next of the smaller pointer to the beginning of the larger chain
    5. set the next of end of larger chain to none so it doesn't loop

    '''

import linked_list

def partition(llist, x):
    checker, smaller, largerfront, largerend = llist.head, llist.head, llist.head, llist.head
    while checker:
        if checker.data < x:
            if smaller != checker:
                smaller.next = checker
                smaller = smaller.next
            if largerfront == checker:
                largerfront = largerfront.next
        if checker.data >= x:
            if largerfront != checker:
                largerend.next = checker
                largerend = largerend.next
            if smaller == checker:
                smaller = smaller.next
                llist.head = checker.next
        checker = checker.next
    smaller.next = largerfront
    largerend.next = None
    return llist.printLL()
            
llist = linked_list.LinkedList()
llist.insertAtBegin(4)
llist.insertAtEnd(4)
llist.insertAtEnd(5)
llist.insertAtEnd(2)
llist.insertAtEnd(1)
llist.insertAtEnd(3)
llist.insertAtEnd(2)
llist.insertAtEnd(3)

print(partition(llist, 3))

'''runtime is O(N) since we are looping through the list once
space complexity is O(1)'''
