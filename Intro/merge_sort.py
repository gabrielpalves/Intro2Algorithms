import time
import numpy as np

def test_function(sort_function):
    elapsed_time = []
    for i in range(5):
        n = 10**i
        seed = 42

        a = np.arange(1, n+1, dtype=int)

        np.random.seed(seed)
        np.random.shuffle(a)

        start_time = time.time()
        a_sorted = sort_function(np.copy(a), 'descend')
        runtime = time.time() - start_time
        print("--- %s seconds for %d numbers ---" % (runtime, n))
        # print('Array:\n{a}\nSorted array:\n{a_sorted}')
        elapsed_time.append(runtime)

    for i in range(len(elapsed_time)):
        print(f'n = {10**i} --> {elapsed_time[i]} seconds')


def merge_sort(array):
    size = array.shape[0]
    if size <= 1:
        return array  # sorted array
    
    # Divide array
    q = int(size/2)
    a1 = array[:q]
    a2 = array[q:]
    
    # Sort the sub-arrays recursively
    a1 = merge_sort(a1)
    a2 = merge_sort(a2)
    
    # Merge the two sub-arrays
    a_merged = np.concatenate((a1, a2))
    j1, j2 = 0, 0
    for j in range(a_merged.shape[0]):
        if j2 >= a2.shape[0]:
            a_merged[j] = a1[j1]
            j1 += 1
        elif j1 >= a1.shape[0]:
            a_merged[j] = a2[j2]
            j2 += 1
        else:
            if a1[j1] < a2[j2]:
                a_merged[j] = a1[j1]
                j1 += 1
            else:
                a_merged[j] = a2[j2]
                j2 += 1

    return a_merged


if __name__ == '__main__':
    test_function(merge_sort)
