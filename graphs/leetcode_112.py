'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

1. Describe the question
do any of the root to leaf paths have a sum that matches the input?
2. What are the constraints
the number of nodes in the tree is in the range [0,5000]
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
3. What are some examples given, and can you solve it by hand?
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Input: root = [1,2,3], targetSum = 5
Output: false
Input: root = [], targetSum = 0
Output: false
4. Any other insights you find
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def hasPathSum(root, targetSum):
    if not root:
        return False
    
    targetSum -= root.val
    if not root.left and not root.right:
        return targetSum == 0
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

