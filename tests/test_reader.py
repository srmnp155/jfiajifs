import unittest
import os
from csv_reader.reader import read_csv

class TestCSVReader(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.csv"
        with open(self.test_file, "w", newline="", encoding="utf-8") as f:
            f.write("name,age\nAlice,30\nBob,25\n")

    def tearDown(self):
        os.remove(self.test_file)

    def test_read_csv(self):
        rows = read_csv(self.test_file)
        expected = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"}
        ]
        self.assertEqual(rows, expected)

if __name__ == "__main__":
    unittest.main()
