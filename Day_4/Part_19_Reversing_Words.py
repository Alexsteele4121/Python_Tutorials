# PART 19: Reversing Words in a string


# We will be making a function that will take a string and reverses each word in the string.
# All spaces in the string should be retained
def reverse_words(string):
    # Your Code Here
    pass


# Everything from here on is testing our software to make sure it operates correctly
import unittest


class Test(unittest.TestCase):
    def test_for_single_reversed_words(self):
        self.assertEqual('gnitset', reverse_words('testing'))
        self.assertEqual('54321', reverse_words('12345'))

    def test_for_multiple_reversed_words(self):
        self.assertEqual('xelA eleetS', reverse_words('Alex Steele'),
                         '[*] The function should keep the words in the same order, '
                         'just reverse the characters within each word.')
        self.assertEqual('54321 9876', reverse_words('12345 6789'))
        self.assertEqual('diD uoy teg ti ot ?krow', reverse_words('Did you get it to work?'))


if __name__ == '__main__':
    unittest.main()
