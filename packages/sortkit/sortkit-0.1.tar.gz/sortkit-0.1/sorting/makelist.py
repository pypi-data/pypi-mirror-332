from sorting.exception_handler import exception_handler

@exception_handler
def makelist(data):
    """Converts various data types (CSV, set, tuple, iterable) to a list while preserving order where possible."""

    # Return if it's already a list
    if isinstance(data, list):
        return data  

    # Convert tuple, range, set to list
    if isinstance(data, (tuple, range, set)):
        return list(data)

    # Convert any iterable (excluding strings/bytes) to list
    if hasattr(data, '__iter__') and not isinstance(data, (str, bytes, bytearray)):
        return list(data)

    # Treat strings and other non-iterables as a single-item list
    return [data]  
