from sorting.exception_handler import exception_handler

@exception_handler
def is_sorted(arr):
    """Checks if the array is sorted."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def custom_shuffle(arr):
    """Implements a simple shuffle algorithm without using `random.shuffle`."""
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = (i * 3) % n  # Custom pseudo-random index generation
        arr[i], arr[j] = arr[j], arr[i]  # Swap elements

def bogo_sort(arr):
    """Sorts the array using Bogo Sort without importing random."""
    while not is_sorted(arr):
        custom_shuffle(arr)
    return arr