'''
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?

1. Describe the question
Removing duplicates from a linked list. 
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
(a,b,c,d,c,e,a,b,e,f) => (a,b,c,d,e,f)
4. Any other insights you find
n = head
list = []
while n:
    if n.data in list:
        prev.next = n.next
    else:
        list.append(n.data)
    prev = n
    n = n.next
return head
'''

import linked_list

def deleteDuplicates(llist):
    n = llist.head
    list = []
    while n:
        if n.data in list:
            prev.next = n.next
        else:
            list.append(n.data)
            prev = n 
        n = n.next
    return llist.printLL()

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

print(deleteDuplicates(llist))

'''runtime is O(N^2) since we are looping through the linked list once and also looking through the list N times. This could be optimized by instead using a hashtable.
space complexity is O(N) since we have to create a new array. 
'''
# using a hashtable instead of an array
def deleteDuplicates2(llist):
    n = llist.head
    hashtable = {}
    while n:
        if n.data in hashtable:
            prev.next = n.next
        else:
            hashtable[n.data] = True
            prev = n 
        n = n.next
    return llist.printLL()

llist2 = linked_list.LinkedList()
 
# add nodes to the linked list
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

print(deleteDuplicates2(llist2))

'''
How can we solve this without using a temporary buffer? (prev pointer)
We can use a runner to loop through along with the original pointer to remove all duplicate letters simultaneously.

head = llist.head
n= head
while n:
    data = n.data
    runner = n.next
    while runner:
        if runner.data == data:
            n.next = runner.next
        runner = runner.next
    n = n.next
return llist.printLL()
            
'''

def deleteDuplicates3(llist):
    n= llist.head
    while n:
        data = n.data
        runner = n
        while runner.next:
            if runner.next.data == data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        n = n.next
    return llist.printLL()

llist3 = linked_list.LinkedList()
 
# add nodes to the linked list
llist3.insertAtBegin('a')
llist3.insertAtEnd('b')
llist3.insertAtEnd('c')
llist3.insertAtEnd('d')
llist3.insertAtEnd('c')
llist3.insertAtEnd('e')
llist3.insertAtEnd('a')
llist3.insertAtEnd('b')
llist3.insertAtEnd('e')
llist3.insertAtEnd('f')

print(deleteDuplicates3(llist3))

'''runtime is now O(N^2) since we are running through the list twice
space complexity is O(1) since we are not using a hashtable
'''