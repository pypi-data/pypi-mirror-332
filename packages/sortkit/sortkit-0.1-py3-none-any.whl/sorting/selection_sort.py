from sorting.exception_handler import exception_handler

@exception_handler
def selection_sort(arr):
    """
    Perform selection sort on a given list.

    :param arr: List of integers or floats
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume current index is the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Compare with min_index
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap elements
    return arr  # Return the sorted array
