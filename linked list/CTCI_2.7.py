'''
Implement a function to check if a linked list is a palindrome.

1. Describe the question
Check if a linked list is a palindrome, meaning if the order were reversed, would it still be the same linked list?
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
(A, B, C, B, A, None) => True
(A, B, C, C, B, A, None) => True
(A) => True
(A, B, A, B) => False
4. Any other insights you find

We need to somehow know when the halfway point in the linked list is in order to start comparing the elements. 
We can do this by having two points, one fast pointer and one slow pointer. 
The fast pointer will move forward twice as fast as the slow pointer, so that once the fast pointer reaches the end of the list, we know that the slow pointer is at the middle.
We can store the first half of the linked list in an array and then compare the second half of the linked list with the elements in the array.

fast = llist.head
slow = llist.head
arr = []

while fast != None and fast.next != None:
    arr.apend(slow.data)
    slow = slow.next
    fast = fast.next.next

if fast != null:
    slow = slow.next

while slow != null:
    if arr.pop() != slow.data:
        return false
    slow = slow.next
return true
'''
import linked_list
def palindrome(llist):
    fast = llist.head
    slow = llist.head
    arr = []

    while fast != None and fast.next != None:
        arr.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast != None:
        slow = slow.next

    while slow != None:
        if arr.pop() != slow.data:
            return False
        slow = slow.next
    return True

llist1 = linked_list.LinkedList()
llist1.insertAtBegin('A')
llist1.insertAtEnd('B')
llist1.insertAtEnd('C')
llist1.insertAtEnd('B')
llist1.insertAtEnd('A')

llist2 = linked_list.LinkedList()
llist2.insertAtBegin('A')
llist2.insertAtEnd('B')
llist2.insertAtEnd('C')
llist2.insertAtEnd('C')
llist2.insertAtEnd('B')
llist2.insertAtEnd('A')

llist3 = linked_list.LinkedList()
llist3.insertAtBegin('A')

llist4 = linked_list.LinkedList()
llist4.insertAtBegin('A')
llist4.insertAtEnd('B')
llist4.insertAtEnd('A')
llist4.insertAtEnd('B')

print(palindrome(llist1))
print(palindrome(llist2))
print(palindrome(llist3))
print(palindrome(llist4))

'''runtime is O(N) since we are only looping through the linked list once.
space complexity is O(N) since we have to store half of the linked list in a new array.'''