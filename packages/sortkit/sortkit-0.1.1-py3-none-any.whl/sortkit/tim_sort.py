from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .exception_handler import exception_handler

@exception_handler
def tim_sort(arr):
    """Python Built-in sorted() based on Tim Sort algorithm, with only one argument."""
    RUN = 32  # Default run size for Tim Sort
    n = len(arr)

    # Step 1: Sort small chunks using Insertion Sort
    for i in range(0, n, RUN):
        arr[i:min(i + RUN, n)] = insertion_sort(arr[i:min(i + RUN, n)])  # Sorting subarrays

    # Step 2: Merge sorted chunks using Merge Sort
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size
            right = min(left + 2 * size, n)
            if mid < right:
                arr[left:right] = merge_sort(arr[left:right])  # Merging subarrays
        size *= 2  # Double the merge size

    return arr
