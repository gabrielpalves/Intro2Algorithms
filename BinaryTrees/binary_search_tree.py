"""
Binary Search Tree (BST) implementation in Python.

BST is a data structure that maintains the order of elements.
It allows for efficient searching, insertion, and deletion operations.
A node contains a key, a left child, a right child, and a parent (null for the root node).

BST property:
1. The left subtree of a node contains only nodes with keys less than or equal to the node's key.
2. The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
"""

import random
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

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
    x = root  # start at root
    # Go downward and find where there is a None
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

# ------------------ Plotting functions ------------------ #

def plot_tree_states(states, titles):
    """Plot multiple BST states side by side."""
    fig, axes = plt.subplots(1, len(states), figsize=(6 * len(states), 6))
    if len(states) == 1:
        axes = [axes]

    for ax, root, title in zip(axes, states, titles):
        G = nx.DiGraph()
        pos = {}

        def add_edges(node, x=0, y=0, depth=0):
            if node is None:
                return
            pos[node] = (x, -depth)
            if node.left:
                G.add_edge(node, node.left)
                add_edges(node.left, x - 2 ** (-depth), y, depth + 1)
            if node.right:
                G.add_edge(node, node.right)
                add_edges(node.right, x + 2 ** (-depth), y, depth + 1)

        add_edges(root)

        colors = []
        for node in G.nodes():
            if node == root:
                colors.append('sandybrown')
            elif node.left is None and node.right is None:
                colors.append('lightgreen')
            else:
                colors.append('lightblue')

        labels = {node: node.key for node in G.nodes()}
        nx.draw(G, pos, ax=ax, labels=labels, with_labels=True, node_size=1000,
                node_color=colors, font_size=10, arrows=True)
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

def clone_tree(node, parent=None):
    """Deep copy a tree rooted at node, preserving structure and keys."""
    if node is None:
        return None
    new_node = Node(node.key)
    new_node.parent = parent
    new_node.left = clone_tree(node.left, new_node)
    new_node.right = clone_tree(node.right, new_node)
    return new_node

# ------------------ Testing ------------------ # 

if __name__ == '__main__':
    state = []
    # Generate a tree
    root = Node(20)
    for i in range(20):
        tree_insert(root, Node(random.randint(0, 40)))
    state.append(clone_tree(root))

    # Testing functions
    ## Print keys in sorted order
    print("Inorder traversal:")
    inorder_tree_walk(root)
    print()

    ## Search for the number k
    k = 28
    print(f"\nSearch for {k}:")
    node_k = tree_search(root, k)
    if node_k:
        print("Found!")
    else:
        print("Not found!")
        node_k = Node(k)  # create node with key k, but do not insert

    ## Minimum and maximum of the tree
    print("\nMinimum:", tree_minimum(root).key)
    print("Maximum:", tree_maximum(root).key)

    ## Successor and predecessor of node with key = k
    successor = tree_successor(node_k)
    print(f"Successor of {k}:", successor.key if successor else "None")

    predecessor = tree_predecessor(node_k)
    print(f"Predecessor of {k}:", predecessor.key if predecessor else "None")

    ## Deletion
    if not tree_search(root, k):  # create node k and insert
        node_k = Node(k)
        tree_insert(root, node_k)  # plot tree after insertion
    state.append(clone_tree(root))

    print("Inorder before deletion:")
    inorder_tree_walk(root)

    print(f"\nDeleting node {k}...")
    tree_delete(root, node_k)
    state.append(clone_tree(root))

    print("Inorder after deletion:")
    inorder_tree_walk(root)

    plot_tree_states(
        state,
        ["Initial Tree", f"After Inserting {k}", f"After Deleting {k}"]
    )
    plt.show()
