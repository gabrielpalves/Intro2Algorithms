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

def Parent(i):
    """Return the index of the parent of the node at index i."""
    return i // 2

def Left_Child(i):
    """Return the index of the left child of the node at index i."""
    return 2 * i

def Right_Child(i):
    """Return the index of the right child of the node at index i."""
    return 2 * i + 1

def Max_Heapify(A, i):
    l = Left_Child(i)
    r = Right_Child(i)
    
    # Find the largest
    if l <= len(A) and A[l] > A[i]:
        largest = l
    elif r <= len(A) and A[r] > A[largest]:
        largest = r
    else:
        largest = i
    
    # If the largest is not the current node, swap and continue heapifying
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest)

def Build_Max_Heap(A):
    """Build a max heap from the given array."""
    # Start from the last non-leaf node and heapify each node
    for i in range(len(A) // 2, 0, -1):
        Max_Heapify(A, i)

def Heapsort(A):
    """Sort the array A using heapsort."""
    Build_Max_Heap(A)
    for i in range(len(A), 1, -1):
        # Swap the root of the heap with the last element
        A[1], A[i] = A[i], A[1]
        # Reduce the size of the heap and heapify the root
        Max_Heapify(A, 1)
