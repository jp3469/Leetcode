'''
Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of
any node never differ by more than one.

1. Describe the question
Given a binary tree, check if the heights of the two subtrees of any node never differ by more than one.
2. What are the constraints
Each subtree in the tree must also satisfy the condition
3. What are some examples given, and can you solve it by hand?
4. Any other insights you find
Use recursion to check if the two subtrees of each node differ in height by no more than one.

if node.left== None and (node.right == None or (node.right.left == None and node.right.right == None):
    return True
else:
    balanced(node.left) and balanced(node.right)
'''
class BinaryTree:
    def __init__(self, node):
        self.root = node

    class Node:
        def __init__(self, content):
            self.content = content
            self.left = None
            self.right = None
            #-1 means the depth has not been calculated yet.
            self.depth = -1

        def __str__(self):
            return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 
    
def balanced(btree):
    if btree is None:
        return True
    else:
        return (abs(depth(btree.left) - depth(btree.right)) <= 1) and balanced(btree.left) and balanced(btree.right)
    
def depth(btree):
    if btree is None:
        return 0
    else:
        if btree.depth != -1:
            return btree.depth
        else:
            btree.depth = 1 + max(depth(btree.left), depth(btree.right))
            return btree.depth

tree = BinaryTree(3)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(1)
tree.right = BinaryTree(6)
tree.right.left = BinaryTree(4)
tree.right.right = BinaryTree(8)
tree.right.right.left = BinaryTree(7)
tree.right.right.right = BinaryTree(9)

print(balanced(tree))

'''runtime is O(N^2) since we have to get the depths of each subtree as well as recurse through the tree to check if it's balanced.
space complexity is O(1).

We could make this more efficient by checking the depth and if it's balanced in the same loop.
'''

def balanced2(btree):
    return check_balanced(btree)[0]
    
def check_balanced(btree):
    if btree is None: return True, 0
    left_balanced, left_depth = check_balanced(btree.left)
    right_balanced, right_depth = check_balanced(btree.right)
    btree.depth = 1 + max(left_depth, right_depth)
    return left_balanced and right_balanced and \
        (abs(depth(btree.left) - depth(btree.right)) <= 1), btree.depth

print(balanced2(tree))


