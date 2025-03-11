from sortkit.exception_handler import exception_handler

@exception_handler
def counting_sort(arr, exp):
    """A helper function for Radix Sort that performs counting sort based on a digit's place value."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """Sorts the array using Radix Sort."""
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr
