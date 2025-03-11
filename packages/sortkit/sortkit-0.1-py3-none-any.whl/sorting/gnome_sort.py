from sorting.exception_handler import exception_handler

@exception_handler
def gnome_sort(arr):
    """Sorts the array using the recursive Gnome Sort algorithm."""
    
    def gnome_recursive(arr, index=0):
        if index >= len(arr):  
            return arr  # Base case: Reached the end, sorting complete
        
        if index == 0 or arr[index] >= arr[index - 1]:  
            return gnome_recursive(arr, index + 1)  # Move forward
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]  # Swap
            return gnome_recursive(arr, index - 1)  # Move backward after swapping

    return gnome_recursive(arr, 0)  # Start recursion from index 0

