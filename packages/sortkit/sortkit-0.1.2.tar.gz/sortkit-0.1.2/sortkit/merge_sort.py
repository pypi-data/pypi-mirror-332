from sortkit.exception_handler import exception_handler

@exception_handler
def merge_sort(arr):
    """
    Perform merge sort on a given list using recursion.

    :param arr: List of integers or floats
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """
    Merge two sorted lists into one sorted list.

    :param left: Sorted list
    :param right: Sorted list
    :return: Merged sorted list
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
