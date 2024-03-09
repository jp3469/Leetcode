'''
Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop

1. Describe the question
Given a circular linked list, find the first node in the list, meaning the first node to be repeated.
2. What are the constraints
3. What are some examples given, and can you solve it by hand? 
(A->B->C->D->E->C) => C
4. Any other insights you find
Loop through the list, and if any node is repeated, that is the beginning of the loop. However, the issue is how can we save the nodes that we have already visited?
Could we use a hashmap?

curr = llist.head
hash = {}
while curr not in hash:
    hash[curr] = True
    curr = curr.next
return curr


'''
import linked_list

def circular(llist):
    curr = llist.head
    hash = {}
    while curr not in hash:
        hash[curr] = True
        curr = curr.next
    return curr

llist1 = linked_list.LinkedList()
llist1.insertAtBegin('A')
llist1.insertAtEnd('B')
llist1.insertAtEnd('C')
llist1.insertAtEnd('D')

curr1 = llist1.head
loop = curr1.next.next
while curr1.next:
    curr1 = curr1.next
curr1.next = loop

print(circular(llist1))
print(circular(llist1).data)

'''runtime of this algorithm is O(N) since we must loop through the list once.
The space complexity will be O(N) since we are creating a hashmap of the size of unique elements in the list.

While this approach works, there is another way to solve this problem without having to create a hashmap.
This is by having two pointers, one slow pointer and one fast pointer. 
The slow pointer would move one step at a time, and the fast pointer would move two steps at a time.
If there is a loop in the list, as the problem says that there is, the two pointers will meet again.
If the non-looped part of the list has length k, the slow pointer will have entered the loop after k steps, meaning the fast pointer will have taken 2k steps. 
In order to find the beginning of the loop from the collision point, we must move both pointers by one k steps.
'''

def findBeginning(linkedlist):
    slow = linkedlist.head
    fast = linkedlist.head

    # Find meetng point
    while (fast != None) and (fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    
    # Check whether it is a circular linked list
    if fast == None or fast.next == None:
        return None

    # Move one runner to head. Making them move at same pace, they will meet at the beginning of the loop
    fast = linkedlist.head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast

nodes_number = 100
nodes_in_loop = 20
L = linked_list.LinkedList()
current = L.head
store = []                 

# Create a linked list
for i in range(nodes_number):
    L.insertAtEnd(i)
    current = L.head if i==0 else current.next
    store.append(current)

# Creat loop
current.next = None if nodes_in_loop <= 0 else store[nodes_number - nodes_in_loop]

beginning = findBeginning(L)
print(beginning.data) 