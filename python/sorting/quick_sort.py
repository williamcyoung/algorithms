def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def partition(array, p, r):
    pivot = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    swap(array, i, j)
    return i + 1

def quickSort(array, p, r):
    q = partition(array, p, r)
    quickSort(array, p, q-1)
    quickSort(array, q+1, r)