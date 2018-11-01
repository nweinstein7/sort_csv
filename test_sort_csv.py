import unittest
import os
from sort_csv import combine_and_sort

TEST_DATA_DIR = 'test_data'
FILE1 = os.path.join(TEST_DATA_DIR, 'small_receive_precedent.csv')
FILE2 = os.path.join(TEST_DATA_DIR, 'small_send_precedent.csv')
OUT = os.path.join(TEST_DATA_DIR, 'out.csv')
EXPECTED = os.path.join(TEST_DATA_DIR, 'expected.csv')

class SortCsvTestCase(unittest.TestCase):
    '''
    Test writing the file
    '''
    maxDiff = None
    def test_create_file(self):
        combine_and_sort(FILE1, FILE2, OUT)
        with open(EXPECTED, 'r') as expected, open(OUT, 'r') as out:
            self.assertMultiLineEqual(expected.read(), out.read())

    def tearDown(self):
        if os.path.isfile(OUT):
            os.remove(OUT)

if __name__ == '__main__':
    unittest.main()