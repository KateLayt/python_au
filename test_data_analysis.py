from data_generator import generate_formated_lst_for_worker
import unittest
from unittest import result
from data_analysis import *

class testing(unittest.TestCase):
    def test_convert_filelines_to_dicts(self):
        filelines = ['[2020-1, 100, 102, 5]', '[2020-1, 200, 203, 10]']
        expect = [{'date': '2020-1', 'storeID': '100', 'staffID': '102', 'amount': '5'}, {'date': '2020-1', 'storeID': '200', 'staffID': '203', 'amount': '10'}]
        result = convert_filelines_to_dicts(filelines)
        self.assertEqual(result, expect)


    def test_get_dicts_for_store(self):
        dicts = [{'date': '2020-1', 'storeID': '100', 'staffID': '102', 'amount': '5'}, {'date': '2020-1', 'storeID': '200', 'staffID': '203', 'amount': '10'}]
        expect = [{'date': '2020-1', 'storeID': '100', 'staffID': '102', 'amount': '5'}]
        result = get_dicts_for_store('100', dicts)
        self.assertEqual(result, expect)

    
    def test_count_store_data(self):
        dicts = [{'date': '2020-1', 'storeID': '100', 'staffID': '102', 'amount': '5'}, {'date': '2020-1', 'storeID': '100', 'staffID': '203', 'amount': '10'}]
        expect = [15, 0 for i in range(11)]
        result = count_store_data(dicts)
        self.assertEqual(result, expect)

    
    def test_generate_formated_lst_for_worker(self):
        data = [1 for i in range(12)]
        expect = [['2020-1', 100, 102, 1], ['2020-2', 100, 102, 1], ['2020-3', 100, 102, 1], ['2020-4', 100, 102, 1], ['2020-5', 100, 102, 1], ['2020-6', 100, 102, 1], ['2020-7', 100, 102, 1], ['2020-8', 100, 102, 1], ['2020-9', 100, 102, 1], ['2020-10', 100, 102, 1], ['2020-11', 100, 102, 1], ['2020-12', 100, 102, 1]]
        result = generate_formated_lst_for_worker(100, 102, data)
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()