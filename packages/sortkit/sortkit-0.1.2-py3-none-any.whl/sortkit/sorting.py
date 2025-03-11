# This file is part of the 'sorting' package.
# This is used for quick sorting of an array.
# This function is called by the main program to sort the array.
from sortkit.insertion_sort import insertion_sort
from sortkit.merge_sort import merge_sort
from sortkit.quick_sort import quick_sort
from sortkit.radix_sort import radix_sort
from sortkit.heap_sort import heap_sort
from sortkit.counting_sort import counting_sort
from sortkit.exception_handler import exception_handler

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

@exception_handler
def sorting(arr):
    n = len(arr)
    
    if is_sorted(arr):
        return arr
    
    elif n <= 20:
        return insertion_sort(arr)
    
    elif 20 < n <= 1000:
        unique_elements = len(set(arr))
        
        if unique_elements <= n // 2:
            return merge_sort(arr)
        
        elif all(isinstance(x, int) for x in arr):
            min_val, max_val = min(arr), max(arr)
            if max_val - min_val < 10_000:
                return counting_sort(arr)
            else:
                return quick_sort(arr)
        
        else:
            return quick_sort(arr)

    elif n > 1000:
        unique_elements = len(set(arr))

        if unique_elements <= n // 10:
            return radix_sort(arr)
        
        elif all(isinstance(x, str) for x in arr):
            return merge_sort(arr)
        
        elif n > 10_000:
            return heap_sort(arr)

        else:
            return quick_sort(arr)

