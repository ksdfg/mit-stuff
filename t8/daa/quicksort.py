from random import choice
from time import time


def _qsort(array, low, high):
    arr = array.copy()
    if low < high:
        i = low
        j = high

        while i < j:
            while i <= high and arr[i] <= arr[low]:
                i += 1
            while j >= low and arr[j] > arr[low]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        return _qsort(arr, low, j - 1) + [arr[j]] + _qsort(arr, j + 1, high)

    elif low == high:
        return [arr[low]]

    else:
        return []


# noinspection DuplicatedCode
def _qsort_random(array, low, high):
    arr = array.copy()
    if low < high:
        pivot = choice(range(low, high + 1))
        i = low
        j = high

        while i < j:
            while i <= high and arr[i] <= arr[pivot]:
                i += 1
            while j >= low and arr[j] > arr[pivot]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]

        return _qsort(arr, low, j - 1) + [arr[j]] + _qsort(arr, j + 1, high)

    elif low == high:
        return [arr[low]]

    else:
        return []


def qsort(array):
    return _qsort(array, 0, len(array) - 1)


def qsort_random(array):
    return _qsort_random(array, 0, len(array) - 1)


if __name__ == '__main__':
    to_sort = [10, 9, 8, 7, 5, 4, 3, 2, 1, 0]

    print("Quicksort")
    print(to_sort)
    start = time()
    sorted = qsort(to_sort)
    end = time()
    print("Sorted array is", sorted)
    print("Time taken is", end - start)

    print("\n-------\n")

    print("Randomised Quicksort")
    print(to_sort)
    start = time()
    sorted = qsort_random(to_sort)
    end = time()
    print("Sorted array is", sorted)
    print("Time taken is", end - start)
