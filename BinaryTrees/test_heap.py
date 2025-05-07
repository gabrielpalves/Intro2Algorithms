from binary_heap import Parent, Left_Child, Right_Child, Max_Heapify, Build_Max_Heap, Heapsort

def test_parent():
    assert Parent(1) == 0
    assert Parent(2) == 0
    assert Parent(3) == 1
    assert Parent(4) == 1
    assert Parent(5) == 2
    assert Parent(6) == 2

def test_left_child():
    assert Left_Child(0) == 1
    assert Left_Child(1) == 3
    assert Left_Child(2) == 5
    assert Left_Child(3) == 7

def test_right_child():
    assert Right_Child(0) == 2
    assert Right_Child(1) == 4
    assert Right_Child(2) == 6
    assert Right_Child(3) == 8

def test_max_heapify_root():
    A = [1, 3, 5]
    Max_Heapify(A, 0)
    assert A == [5, 3, 1]  # Max at root

def test_max_heapify_subtree():
    A = [10, 20, 5, 1, 2]
    Max_Heapify(A, 1)
    assert A == [10, 20, 5, 1, 2]  # Already a max-heap subtree

def test_max_heapify_swap_needed():
    A = [10, 2, 5, 1, 20]
    Max_Heapify(A, 1)
    assert A == [10, 20, 5, 1, 2]  # Swap 2 with 20

def test_max_heapify_recursive():
    A = [1, 20, 5, 3, 2]
    Max_Heapify(A, 0)
    assert A == [20, 3, 5, 1, 2]  # 1 swaps with 20, then 1 swaps with 3

def is_max_heap(A):
    """Helper function to verify if A satisfies the max-heap property."""
    n = len(A)
    for i in range(n // 2):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and A[i] < A[l]:
            return False
        if r < n and A[i] < A[r]:
            return False
    return True

def test_build_max_heap_basic():
    A = [3, 5, 1, 10, 2]
    Build_Max_Heap(A)
    assert is_max_heap(A)

def test_build_max_heap_sorted():
    A = [1, 2, 3, 4, 5, 6]
    Build_Max_Heap(A)
    assert is_max_heap(A)

def test_build_max_heap_reverse_sorted():
    A = [6, 5, 4, 3, 2, 1]
    Build_Max_Heap(A)
    assert is_max_heap(A)

def test_build_max_heap_single_element():
    A = [42]
    Build_Max_Heap(A)
    assert is_max_heap(A)

def test_build_max_heap_duplicates():
    A = [4, 4, 4, 4]
    Build_Max_Heap(A)
    assert is_max_heap(A)

def test_heapsort_basic():
    A = [3, 5, 1, 10, 2]
    Heapsort(A)
    assert A == sorted(A)  # Check if sorted
