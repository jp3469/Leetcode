'''
tree- a set of nodes storing elements such that the nodes have a parent child relationship
root- special node that has no parent
parent, child- every node with parent w is a child of w
siblings- two nodes that are children of the same parent 
external node(leaves)- node with no children
internal node- node with one or more children
ancestor- node u is an ancestor of node v if u=v or u is an ancestor of the parent of v
descendant- node v is a descendant of node u if u is an ancestor of v
subtree- the tree consisting of all the descendants including itself
edge- a pair of nodes where one is the parent of the other
path- sequence of nodes such that any two consecutive nodes is an edge
ordered tree- there is a meaningful linear order among the children of each node
BST- binary tree in which each node has at most two children, left child and right child and for any given onde, 
    all nodes in its right subtree have values greater than the node's value and all nodes in its left subtree
    have values less than or equal to the node's value
when it's just a binary tree, you don't need a tree class. the root node is sufficient to refer to the tree.
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def find_min(self, node):
        if node.left is None:
            return node
        return self.find_min(node.left)
    
    def delete_node(self, root, value):
        if root is None:
            return root
        
        if value < root.data:
            root.left = self.delete_node(root.left, value)
        elif value > root.data:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        
        return root
    
    def delete_method(self, value):
        self.root = self.delete_node(self.root, value)
    
    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = None
            
            while current is not None:
                parent = current
                if value < current.data:
                    current = current.left
                else:
                    current = current.right
            
            if value < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node
    
    def search(self, value):
        current = self.root
        while current is not None:
            if current.data == value:
                return True
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        return False
    
    def in_order_helper(self, node):
        if node is not None:
            self.in_order_helper(node.left)
            print(node.data, end=" ")
            self.in_order_helper(node.right)
    
    def in_order(self):
        self.in_order_helper(self.root)
        print()
    
    def pre_order_helper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)
    
    def pre_order(self):
        self.pre_order_helper(self.root)
        print()
    
    def post_order_helper(self, node):
        if node is not None:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data, end=" ")
    
    def post_order(self):
        self.post_order_helper(self.root)
        print()

# Main function
if __name__ == "__main__":
    obj = BST()
    obj.insert(5)
    obj.insert(3)
    obj.insert(7)
    obj.insert(2)
    obj.insert(4)
    obj.insert(6)
    obj.insert(8)
    
    obj.in_order()
    obj.pre_order()
    obj.post_order()

    obj.delete_method(2)

    obj.in_order()


