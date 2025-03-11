from sortkit.exception_handler import exception_handler

@exception_handler
def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    ---------------------
    Repeatedly swaps adjacent elements if they are in the wrong order.

    :param arr: List of numbers to be sorted
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:
            break  # Stop if already sorted
    return arr
