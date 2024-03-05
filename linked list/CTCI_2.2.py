'''
Implement an algorithm to find the kth to the last element of a singly linked list.

1. Describe the question
Find the kth last element in a singly linked list
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
(a,b,c,d,c,e,a,b,e,f) 1 => f
(a,b,c,d,c,e,a,b,e,f) 2 => e
(a,b,c,d,c,e,a,b,e,f) 3 => b
(a,b,c,d,c,e,a,b,e,f) 4 => a
(a,b,c,d,c,e,a,b,e,f) 2 => e
(a,b,c,d,c,e,a,b,e,f) 2 => c
(a,b,c,d,c,e,a,b,e,f) 2 => d
(a,b,c,d,c,e,a,b,e,f) 2 => c
(a,b,c,d,c,e,a,b,e,f) 2 => b
(a,b,c,d,c,e,a,b,e,f) 2 => a
4. Any other insights you find
the method I can initially think of is traversing to the end of the list to find the length of the array and then traversing through once again to find the correct element

n = llist.head
count = n
length = 0
while count:
    length += 1
    count = count.next
index = length - k
for i in range(index):
    n = n.next
return n.data
'''
import linked_list
def kthlast(llist, k):
    n = llist.head
    count = n
    length = 0
    while count:
        length += 1
        count = count.next
    index = length - k
    for _ in range(index):
        n = n.next
    return n.data

llist = linked_list.LinkedList()
 
# add nodes to the linked list
llist.insertAtBegin('a')
llist.insertAtEnd('b')
llist.insertAtEnd('c')
llist.insertAtEnd('d')
llist.insertAtEnd('c')
llist.insertAtEnd('e')
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtEnd('e')
llist.insertAtEnd('f')

print(kthlast(llist, 1))
print(kthlast(llist, 2))
print(kthlast(llist, 3))
print(kthlast(llist, 4))
print(kthlast(llist, 5))
print(kthlast(llist, 6))
print(kthlast(llist, 7))
print(kthlast(llist, 8))
print(kthlast(llist, 9))
print(kthlast(llist, 10))

'''runtime will be O(N^2) since we have to loop through the list twice.
space complexity is O(1) since no space is allocated. 

use two pointers that are k distance apart, and once the farther pointer reaches the end, we know that we are at the kth to last element.

head = llist.head
tail = head
for _ in range(k):
    tail = tail.next
while tail:
    tail = tail.next
    head = head.next
return head.data

'''

def kthlast2(llist, k):
    head = llist.head
    tail = head
    for _ in range(k-1):
        tail = tail.next
    while tail.next:
        tail = tail.next
        head = head.next
    return head.data

llist2 = linked_list.LinkedList()
llist2.insertAtBegin('a')
llist2.insertAtEnd('b')
llist2.insertAtEnd('c')
llist2.insertAtEnd('d')
llist2.insertAtEnd('c')
llist2.insertAtEnd('e')
llist2.insertAtEnd('a')
llist2.insertAtEnd('b')
llist2.insertAtEnd('e')
llist2.insertAtEnd('f')

print(kthlast2(llist2, 1))
print(kthlast2(llist2, 2))
print(kthlast2(llist2, 3))
print(kthlast2(llist2, 4))
print(kthlast2(llist2, 5))
print(kthlast2(llist2, 6))
print(kthlast2(llist2, 7))
print(kthlast2(llist2, 8))
print(kthlast2(llist2, 9))
print(kthlast2(llist2, 10))

'''runtime is now O(N) since we are only iterating through the list once
space is still O(1)'''