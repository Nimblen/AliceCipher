import unittest
from alice import remove_pairs


class TestRemovePairs(unittest.TestCase):

    def test_remove_pairs(self):
        self.assertEqual(remove_pairs("aaabbb"), "ab")
        self.assertEqual(remove_pairs("hello world"), "heo world")
        self.assertEqual(remove_pairs("aaabbcccaaa"), "aca")


if __name__ == '__main__':
    unittest.main()