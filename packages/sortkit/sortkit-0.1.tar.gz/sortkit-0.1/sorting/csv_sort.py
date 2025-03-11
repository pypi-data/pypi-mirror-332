# Description: Sorts a CSV file or list of lists based on a specific column.
def csv_sort(data, column_index=0):
    """Sorts a CSV file or list of lists based on a specific column."""
    
    # Check if input is a file path (string), then read its content
    if isinstance(data, str):
        with open(data, "r", encoding="utf-8") as file:
            lines = file.readlines()
        data = [line.strip().split(",") for line in lines]  # Convert to list of lists

    # Extract header and data separately
    header, rows = data[0], data[1:]

    # Sort the data based on the specified column
    sorted_data = sorted(rows, key=lambda row: row[column_index].strip().lower())

    return [header] + sorted_data  # Return sorted data including the header
