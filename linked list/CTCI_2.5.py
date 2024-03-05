''' 
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order,
such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

1. Describe the question
Two numbers are represented as a linked list in reverse order. Write a function that adds the two numbers and returns the sum as a linked list.
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
(7,1,6), (5,9,2) => (2,1,9)
(7,1), (5,9,2) => (2,1,3)
4. Any other insights you find
since the list is in reverse order, we don't have to worry about if the two lists are of different length since, the ones digit will always be at the front

result = linked_list.LinkedList()
resultend = result.head
head1 = llist1.head
head2 = llist2.head
carry = 0
while head1 and head2:
    resultend.data = (head1.data + head2.data) % 10 + carry
    resultend.next = Node(0)
    resultend = resultend.next
    carry = head1.data + head2.data + carry > 9
    head1, head2 = head1.next, head2.next
if head1:
    while head1:
        resultend.data = head1.data + carry
        resultend.next = Node(0)
        resultend = resultend.next
        head1 = head1.next
        carry = 0
elif head2:
    while head2:
        resultend.data = head2.data + carry
        resultend.next = Node(0)
        resultend = resultend.next
        head2 = head2.next
        carry = 0
return result.printLL()


'''
import linked_list

def sumList(llist1, llist2):
    result = linked_list.LinkedList()
    head1 = llist1.head
    head2 = llist2.head
    carry = 0
    while head1 and head2:
        result.insertAtEnd((head1.data + head2.data + carry) % 10)
        carry = head1.data + head2.data + carry > 9
        head1, head2 = head1.next, head2.next
    if head1:
        while head1:
            result.insertAtEnd(head1.data + carry)
            head1 = head1.next
            carry = 0
    elif head2:
        while head2:
            result.insertAtEnd(head2.data + carry)
            head2 = head2.next
            carry = 0
    elif carry == 1:
        result.insertAtEnd(1)
    return result.printLL()

llist1 = linked_list.LinkedList()
llist1.insertAtBegin(7)
llist1.insertAtEnd(1)
llist1.insertAtEnd(7)

llist2 = linked_list.LinkedList()
llist2.insertAtEnd(5)
llist2.insertAtEnd(9)
llist2.insertAtEnd(2)

print(sumList(llist1, llist2))

'''runtime is O(N) since we're looping through each list just once
space complexity is O(N) since we are creating and returning a new linked list'''

'''
FOLLOW UP 
Suppose the digits are stored in forward order. Repeat the above problem. 


'''