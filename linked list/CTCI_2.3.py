'''
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node

1. Describe the question
Deleting a certain node in the middle of a singly linked list, but you are only given access to that node and not the head
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
Given node c from the linked list a->b->c->d->e, the result should be nothing returned but the linked should look like a->b->d->e
4. Any other insights you find
Since we are not given access to the head of the node, we can't find the node previous to the middle node provided.
Therefore, the only solution is to copy the data from the next node and move it into the provided node and delete the next node.

new = node.next.data
node.data = new
node.next = node.next.next
'''
import linked_list
def deleteMiddle(N):
    new = N.next.data
    N.data = new
    N.next = N.next.next

llist = linked_list.LinkedList()
llist.insertAtBegin('a')
llist.insertAtEnd('b')
llist.insertAtEnd('c')
llist.insertAtEnd('d')
llist.insertAtEnd('e')
N1 = llist.head.next
deleteMiddle(N1)
llist.printLL()

llist2 = linked_list.LinkedList()
llist2.insertAtBegin('a')
llist2.insertAtEnd('b')
llist2.insertAtEnd('c')
llist2.insertAtEnd('d')
llist2.insertAtEnd('e')
N2 = llist2.head.next.next
deleteMiddle(N2)
llist2.printLL()

llist3 = linked_list.LinkedList()
llist3.insertAtBegin('a')
llist3.insertAtEnd('b')
llist3.insertAtEnd('c')
llist3.insertAtEnd('d')
llist3.insertAtEnd('e')
N3 = llist3.head.next.next.next
deleteMiddle(N3)
llist3.printLL()

'''runtime is O(1) and space complexity is also O(1)'''
