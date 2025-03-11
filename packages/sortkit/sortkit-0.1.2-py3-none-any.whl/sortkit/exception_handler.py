def exception_handler(func):
    """Decorator to handle exceptions globally for sorting functions, ensuring input is converted to a list before sortkit."""
    
    def wrapper(data):
        try:
            data = to_list(data)  # Convert input to a list before sorting
            return func(data)  # Now sort the processed list
            
        except FileNotFoundError:
            raise FileNotFoundError("CSV file not found.")
        except TypeError as te:
            raise TypeError(f"Type Error: {te}")
        except ValueError as ve:
            raise ValueError(f"Value Error: {ve}")
        except MemoryError:
            raise MemoryError("Input is too large!")
        except Exception as e:
            raise Exception(f"Unexpected Error: {e}")

    return wrapper


def to_list(data):
    """Converts various data types (CSV, set, tuple, iterable) to a list while preserving order where possible."""
    
    # Convert CSV file to list of lists
    if isinstance(data, str) and data.endswith(".csv"):
        with open(data, "r", encoding="utf-8") as file:
            return [line.strip().split(",") for line in file]

    # Convert tuple to list (preserves order)
    if isinstance(data, tuple):
        return list(data)
    
    # Convert set to list (order may change)
    if isinstance(data, set):
        return list(data)

    # Convert any iterable (excluding strings/bytes) to list
    if hasattr(data, '__iter__') and not isinstance(data, (str, bytes, bytearray)):
        return list(data)
    
    # Return if it's already a list
    if isinstance(data, list):
        return data

    # Raise error for unsupported types
    raise TypeError("Input must be a list, set, tuple, iterable (excluding strings), or a CSV file.")

