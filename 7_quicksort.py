import numpy as np

def partition(A, p ,r):
    x = A[r-1]
    i = p-1
    for j in range(p, r):
        if A[j-1] <= x:
            i += 1
            A[i-1], A[j-1] = A[j-1], A[i-1]
    A[i], A[r-1] = A[r-1], A[i]
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

A = range(63)
np.random.shuffle(A)
print A
quicksort(A, 1, len(A))
print A
