# We will write test cases for all sorting algorithms in this file
import unittest
from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort,heap_sort, counting_sort ,gnome_sort, string_sort , sorting, shell_sort, bogo_sort,bucket_sort,tim_sort,comb_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ([5, 3, 8, 6, 2, 7, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
            ([100, 50, 25, 75, 10], [10, 25, 50, 75, 100]),
            ([3], [3]),
            ([], []),
            ([1, 3, 2, 3, 1], [1, 1, 2, 3, 3])  # Duplicates
        ]

    def test_bubble_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(bubble_sort(arr[:]), expected)

    def test_selection_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(selection_sort(arr[:]), expected)

    def test_insertion_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(insertion_sort(arr[:]), expected)

    def test_quick_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(quick_sort(arr[:]), expected)

    def test_merge_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(merge_sort(arr[:]), expected)

    def test_heap_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(heap_sort(arr[:]), expected)
                
    def test_shell_sort(self):
        for inp, expected in self.test_cases:
            self.assertEqual(shell_sort(inp[:]), expected)


    def test_bogo_sort(self):
        # Bogo Sort is highly inefficient, so we test only small inputs
        self.assertEqual(bogo_sort([3, 1, 2]), [1, 2, 3])
        
    
    def test_bucket_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(bucket_sort(arr[:]), expected)    
    
    def test_tim_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(tim_sort(arr[:]), expected)    

    def test_comb_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(comb_sort(arr[:]), expected)  

    def test_gnome_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(gnome_sort(arr[:]), expected)  
                                
    def test_counting_sort(self):
      for arr, expected in self.test_cases:
        if all(isinstance(x, (int, float)) for x in arr):  # Counting Sort supports both integers & floats
            with self.subTest(arr=arr):
                try:
                    self.assertEqual(counting_sort(arr[:]), expected)
                except TypeError:
                    self.fail("counting_sort() raised TypeError unexpectedly!")
                    
    
    def test_string_sort(self):
        string_cases = [
            (["apple", "banana", "orange", "grape"], ["apple", "banana", "grape", "orange"]),
            (["zebra", "lion", "tiger", "elephant"], ["elephant", "lion", "tiger", "zebra"]),
        ]
        for inp, expected in string_cases:
            self.assertEqual(string_sort(inp[:]), expected)                

    def test_sorting(self):
        for inp, expected in self.test_cases:
            self.assertEqual(sorting(inp[:]), expected)  # Assuming this is a general sorting wrapper function



if __name__ == "__main__":
    unittest.main()
