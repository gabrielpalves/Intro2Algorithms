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
        a_sorted = sort_function(np.copy(a))
        runtime = time.time() - start_time
        print("--- %s seconds for %d numbers ---" % (runtime, n))
        # print('Array:\n{a}\nSorted array:\n{a_sorted}')
        elapsed_time.append(runtime)

    for i in range(len(elapsed_time)):
        print(f'n = {10**i} --> {elapsed_time[i]} seconds')


def insertion_sort(array):
    for j in range(1, array.shape[0]):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        
        array[i + 1] = key
    
    return array


if __name__ == '__main__':
    test_function(insertion_sort)
