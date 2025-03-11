from sorting.exception_handler import exception_handler

@exception_handler
def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Update count[i] to store the cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output