from .exception_handler import exception_handler

@exception_handler
def string_sort(strings):
    """Sorts a list of strings in lexicographical order (case-insensitive but preserves original case)."""
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise TypeError("Input must be a list of strings.")
    
    return sorted(strings, key=str.lower)  # Case-insensitive sort