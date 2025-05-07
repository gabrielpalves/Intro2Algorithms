"""    
Binary Heap Implementation in Python

A heap (binary) is a data structure that can be seen as a complete binary tree.
It is a special case of the more general data structure called a priority queue.
A heap is a complete binary tree that satisfies the heap property:
- In a max heap, for any given node I, the value of I is greater than or equal to the values of its children.
- In a min heap, the value of I is less than or equal to the values of its children.

For a vector A to be a max heap, it must satisfy the following property:
A[Parent(i)] >= A[i] for all i > 1.

- The height of a node of the tree is the number of edges in the longest path of the node downto a leaf of the tree.
- The tree height is the height of the root node.
- Since a heap induces a binary tree, its height is Θ(log n).
"""

import random
import matplotlib.pyplot as plt
import networkx as nx
import imageio


# ----------------------------------------------------
# Visualize the heap using NetworkX and Matplotlib
# ----------------------------------------------------
def visualize_heap(A, title="", pause=1.0, current_node=None, changed_nodes=None):
    G = nx.DiGraph()
    labels = {}
    
    # Default values if not provided
    if changed_nodes is None:
        changed_nodes = []
    
    # Create nodes and edges
    for i, value in enumerate(A):
        labels[i] = str(value)
        left = Left_Child(i)
        right = Right_Child(i)
        if left < len(A):
            G.add_edge(i, left)
        if right < len(A):
            G.add_edge(i, right)
    
    pos = hierarchy_pos(G, 0)
    
    # Determine node colors
    node_colors = []
    for i in G.nodes():
        if i == current_node:
            node_colors.append('red')  # Current node being evaluated
        elif i in changed_nodes:
            node_colors.append('lightgreen')  # Nodes that were changed
        else:
            node_colors.append('lightblue')  # Default color
    
    plt.clf()
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, 
            node_size=1200, font_size=15)
    plt.title(title, fontsize=16)
    plt.pause(pause)

def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
    def _hierarchy_pos(G, root, leftmost, width, vert_gap, vert_loc, xcenter, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if children:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, leftmost, dx, vert_gap, vert_loc - vert_gap, nextx, pos, root)
        return pos
    return _hierarchy_pos(G, root, 0, width, vert_gap, vert_loc, xcenter)

# ----------------------------------------------------
# Binary Heap Functions
# ----------------------------------------------------
def Parent(i):
    """Return the index of the parent of the node at index i."""
    return (i - 1) // 2

def Left_Child(i):
    """Return the index of the left child of the node at index i."""
    return 2 * i + 1

def Right_Child(i):
    """Return the index of the right child of the node at index i."""
    return 2 * i + 2

def Max_Heapify(A, i, full_array=None):
    """Ensure the subtree rooted at index i is a max heap."""
    if full_array is None:
        full_array = A
    l = Left_Child(i)
    r = Right_Child(i)
    n = len(A) - 1
    
    # Find the largest
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r <= n and A[r] > A[largest]:
        largest = r
    
    # If the largest is not the current node, swap and continue heapifying
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        # Update the full array if we're working with a slice
        if full_array is not A:
            full_array[i], full_array[largest] = A[i], A[largest]
        visualize_heap(full_array, title=f"Heapify at index {i}", 
                      current_node=i, changed_nodes=[i, largest])
        Max_Heapify(A, largest, full_array)
    else:
        visualize_heap(full_array, title=f"Heapify at index {i}", 
                      current_node=i)

def Build_Max_Heap(A):
    """Build a max heap from the given array."""
    # Start from the last non-leaf node and max-heapify each node
    for i in range(len(A) // 2 - 1, -1, -1):
        visualize_heap(A, title=f"Building heap at index {i}", current_node=i)
        Max_Heapify(A, i)

def Heapsort(A):
    """Sort the array A using heapsort."""
    Build_Max_Heap(A)
    heap_size = len(A)
    
    plt.figure()
    for i in range(heap_size-1, 0, -1):
        # Swap the root with the last element
        A[0], A[i] = A[i], A[0]
        
        visualize_heap(A, title=f"Sorting - swapped {A[i]} with root", 
                      current_node=0, changed_nodes=[0, i])
        
        # Heapify the reduced heap but visualize the full array
        temp_heap = A[:i]
        Max_Heapify(temp_heap, 0, full_array=A)
        A[:i] = temp_heap


if __name__ == "__main__":
    n = 10
    a = 0
    b = 50

    A = [random.randint(a, b) for _ in range(n)]
    print("Original array:", A)

    plt.ion()
    Heapsort(A)
    plt.ioff()
    plt.show()

    print("Sorted array:", A)
