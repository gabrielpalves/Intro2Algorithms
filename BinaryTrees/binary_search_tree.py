"""
Binary Search Tree (BST) implementation in Python.

BST is a data structure that maintains the order of elements.
It allows for efficient searching, insertion, and deletion operations.
A node contains a key, a left child, a right child, and a parent (null for the root node).

BST property:
1. The left subtree of a node contains only nodes with keys less than or equal to the node's key.
2. The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
"""

def inorder_tree_walk(node):
    """Prints all the keys in the BST in sorted order."""
    if node is not None:
        inorder_tree_walk(node.left)
        print(node.key, end=' ')
        inorder_tree_walk(node.right)

def tree_search(node, key):
    """Returns a pointer to a node with key k if one exists, otherwise None."""
    if node is None or key == node.key:
        return node
    if key < node.key:
        return tree_search(node.left, key)
    else:
        return tree_search(node.right, key)

def iterative_tree_search(node, key):
    """tree_search implemented iteratively instead of recursively."""
    while node is not None and key != node.key:
        if key < node.key:
            node = node.left
        else:
            node = node.right
    return node

def tree_minimum(node):
    """Returns the node with the minimum key in the subtree rooted at node."""
    while node.left is not None:
        node = node.left
    return node

def tree_maximum(node):
    """Returns the node with the maximum key in the subtree rooted at node."""
    while node.right is not None:
        node = node.right
    return node

def tree_successor(node):
    """Returns the successor of a node in the BST."""
    if node.right is not None:
        # Just have to search the leftmost node in the right subtree
        return tree_minimum(node.right)
    # If there is no right subtree, the successor is one of the ancestors
    # We go up until we find a node that is the left child of its parent
    # Then the parent will be the successor,
    # which is the first node that is greater than the current node
    y = node.parent
    while y is not None and node == y.right:
        node = y
        y = y.parent
    return y

def tree_predecessor(node):
    """Returns the predecessor of a node in the BST."""
    if node.left is not None:
        # Just have to search the rightmost node in the left subtree
        return tree_maximum(node.left)
    # If there is no left subtree, the predecessor is one of the ancestors
    # We go up until we find a node that is the right child of its parent
    # Then the parent will be the predecessor,
    # which is the first node that is less than the current node
    y = node.parent
    while y is not None and node == y.left:
        node = y
        y = y.parent
    return y

def tree_insert(root, node):
    """Insert a node in the correct position.
    
    Begins at the root of the tree and goes downward to find a None to replace with node.
    The trailing pointer y is the parent of x."""
    y = None
    x = root
    while x is not None:
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right
    # Insert node in a left or right leaf, below the parent (y)
    node.parent = y
    if y == None:
        root = node  # Tree was empty
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node

def tree_delete(root, node):
    """Delete a node and adjust the BST.
    
    1. If node has no children, just delete it.
    Its parent will now have a None.
    2. If node has only one child, the child is elevated, taking the node position.
    The parent of node will replace node for its child.
    3. If node has two children, find node's successor y, then y take node's position.
    The rest of node's right subtree becomes the right subtree of y,
    and the node's left subtree becomes the y's left subtree."""
    def transplant(root, node_u, node_v):
        """Replaces one subtree as a child of its parent with another subtree."""
        if node_u.parent == None:
            root = node_v
        elif node_u == node_u.parent.left:
            node_u.parent.left = node_v
        else:
            node_u.parent.right = node_v
        if node_v != None:
            node_v.parent = node_u.parent
    
    if node.left == None:
        transplant(root, node, node.right)
    elif node.right == None:
        transplant(root, node, node.left)
    else:
        y = tree_minimum(node.right)
        if y.parent != node:
            transplant(root, y, y.right)
            y.right = node.right
            y.right.parent = y
        transplant(root, node, y)
        y.left = node.left
        y.left.parent = y
