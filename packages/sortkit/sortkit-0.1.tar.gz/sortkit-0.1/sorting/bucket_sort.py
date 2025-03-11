from sorting.exception_handler import exception_handler

@exception_handler
def bucket_sort(arr):
    """Sorts the array using Bucket Sort only if it is not empty."""
    if arr:  # Executes only if arr is not empty
        bucket_count = len(arr)
        max_val, min_val = max(arr), min(arr)

        if max_val == min_val:  # If all elements are the same, return early
            return arr

        bucket_range = (max_val - min_val) / bucket_count
        buckets = [[] for _ in range(bucket_count)]

        for num in arr:
            index = int((num - min_val) / bucket_range)
            index = min(index, bucket_count - 1)  # Ensure index is within range
            buckets[index].append(num)

        sorted_arr = []
        for bucket in buckets:
            if bucket:  # Skip empty buckets
                bucket.sort()
                sorted_arr.extend(bucket)

        return sorted_arr
    
    # If the array is empty, do nothing (or return None)
    return arr

