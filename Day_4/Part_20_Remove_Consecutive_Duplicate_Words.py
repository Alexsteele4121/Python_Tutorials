# PART 20: Remove Consecutive Duplicate Words


# This function will except a string and remove any consecutive duplicates that we find and return the result.
def remove_consecutive_duplicates(string):
    # Your Code Here
    pass


# Everything from here on is testing our software to make sure it operates correctly
import unittest


class Test(unittest.TestCase):
    def test_for_duplicates(self):
        self.assertEqual('Hello World!', remove_consecutive_duplicates('Hello Hello World!'))
        self.assertEqual('123 2 123 678', remove_consecutive_duplicates('123 2 2 123 123 678'))
        self.assertEqual('a L l e x S T e l E', remove_consecutive_duplicates('a a a L l e x x x S T T e l l E'))


if __name__ == '__main__':
    unittest.main()
