from sortkit.exception_handler import exception_handler

@exception_handler
def comb_sort(arr):
    """Sorts the array using recursive Comb Sort algorithm with only one argument."""
    
    def comb_recursive(arr, gap):
        """Recursive helper function for Comb Sort."""
        gap = max(1, int(gap / 1.3))  # Reduce gap using shrink factor 1.3
        swapped = False

        # Perform one pass with the current gap
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

        # Base case: Stop when gap is 1 and no swaps happened
        if gap == 1 and not swapped:
            return arr

        # Recursive call
        return comb_recursive(arr, gap)

    return comb_recursive(arr, len(arr))  # Initial call with full array length
