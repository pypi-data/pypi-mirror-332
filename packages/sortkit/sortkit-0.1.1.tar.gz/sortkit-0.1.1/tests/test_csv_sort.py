# We will write a test case for the csv_sort function in this file.
import unittest
from sorting import csv_sort  # Importing your function

class TestCSVSort(unittest.TestCase):

    def setUp(self):
        """Set up test data for sorting."""
        self.test_data = './tests/test_csv.csv'

    def test_csv_sort_by_name(self):
        """Test sorting the CSV data by the 'Name' column."""
        result = csv_sort(self.test_data, 0)  # Pass data directly
        print("Sorted Output:")
        for row in result:
            print(row)

if __name__ == "__main__":
    unittest.main()
