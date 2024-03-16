import unittest
from utils.excel_reader import get_excel_data


class ExcelDataReaderTest(unittest.TestCase):
    """Testing for excel_data_reader"""

    def test_get_excel_data_by_row_col_name(self):
        """Should get excel value by Row name (Col A) and Column name (Row 1)"""

        data = get_excel_data("test.xlsx", "Y20", "Income")
        self.assertEqual(data, 120000)

    def test_get_excel_data_by_row_col_index(self):
        """Should get excel value by Row name (Col A) and Column name (Row 1)"""
        data = get_excel_data("test.xlsx", 2, 1)
        self.assertEqual(data, 125000)


if __name__ == '__main__':
    unittest.main()
