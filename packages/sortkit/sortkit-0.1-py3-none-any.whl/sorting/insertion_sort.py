from sorting.exception_handler import exception_handler

@exception_handler
def insertion_sort(arr):
    """
    Perform insertion sort on a given list.

    :param arr: List of integers or floats
    :return: Sorted list
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  # Return the sorted array
