# PART 21: Find the shortest word

# This function should find the shortest word in a string a return the length of it.
def find_shortest(string):
    # Your Code Here
    pass


# Everything from here on is testing our software to make sure it operates correctly
import unittest


class Test(unittest.TestCase):
    def test_for_shortest(self):
        self.assertEqual(3, find_shortest('Testing for the shortest words'))
        self.assertEqual(2, find_shortest('Are we learning some python?'))
        self.assertEqual(5, find_shortest('Hello World!'))
        self.assertEqual(5, find_shortest('Forever Fives'))


if __name__ == '__main__':
    unittest.main()
