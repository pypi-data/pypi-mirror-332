from sortkit.exception_handler import exception_handler

@exception_handler
def quick_sort(arr):
    """
    Perform Quick sort on a given list.

    :param arr: List of integers or floats
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)