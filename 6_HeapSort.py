import math
import numpy as np


def parent(i):
    return i >> 1


def left(i):
    return i << 1


def right(i):
    return (i << 1) + 1


def max_heap_property_CHECK(A):
    for i in range(1, len(A)):
        if A[parent(i)] > A[i]:
            return False
    return True


def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A, heap_size):
    for i in range(parent(len(A)), -1, -1):
        max_heapify(A, i, heap_size)


def heap_sort(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)


def tree_print_line(n):
    line = ""
    for i in range((1 << n) - 1, min((1 << n + 1) - 1, len(A))):
        line += str(A[i]).zfill(2)
        if i != (1 << n) - 2:
            line += " "
    return line


def tree_print(A):
    height = int(math.log(len(A), 2)) + 1
    for i in range(height):
        print tree_print_line(i).center(20 * height)


A = range(63)
np.random.shuffle(A)
print A
print max_heap_property_CHECK(A)
heap_sort(A)
print A
print max_heap_property_CHECK(A)

# tree_print(A)
