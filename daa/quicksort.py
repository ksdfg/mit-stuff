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
    
    
def qsort(array):
    return _qsort(array, 0, len(array)-1)


if __name__ == '__main__':
    to_sort = [10, 7, 8, 9, 1, 5]
    print(to_sort, qsort(to_sort))