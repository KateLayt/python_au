import unittest
from generate_md import *

class testing(unittest.TestCase):
    def test_read_all_lines_from(self):
        result = read_all_lines_from("test.txt")
        expect = ['#111. TaskName\n', '#https://leetcode.com/problems/\n', 'class Solution:']
        self.assertEqual(result, expect)

    def test_merge_solutions(self):
        old = ['beginning ', '[comment]: <> (Stop)', 'end']
        new = 'newbeginning '
        result = merge_solutions(old, new)
        expect = 'newbeginning end'
        self.assertEqual(result, expect)

    def test_get_md_title(self):
        testfile = read_all_lines_from("test.txt")
        source = LeetCodeSolution(testfile[0], testfile[1], testfile[2:])
        result = source.get_md_title()
        expect = "## TaskName"
        self.assertEqual(result, expect)
      
    def test_get_title_link(self):
        testfile = read_all_lines_from("test.txt")
        source = LeetCodeSolution(testfile[0], testfile[1], testfile[2:])
        result = source.get_title_link()
        expect = "+ [TaskName](#)"
        self.assertEqual(result, expect)

    def test_get_md_solution(self):
        testfile = read_all_lines_from("test.txt")
        source = LeetCodeSolution(testfile[0], testfile[1], testfile[3:])
        result = source.get_md_solution()
        expect = "+ [TaskName](#)\n\n[comment]: <> (Stop)\n\n## TaskName\n\nhttps://leetcode.com/problems/\n\n``` python\n```"
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()