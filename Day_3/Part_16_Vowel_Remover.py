# PART 16: Removing Vowels from a string


# Here we'll be making a function that will remove all vowels from a string and return the resulting string.
def vowel_remover(string):
    # Your Code Here
    pass


# Everything from here on is testing our software to make sure it operates correctly
import unittest


class Test(unittest.TestCase):
    def test_for_vowels(self):
        self.assertEqual('tstng', vowel_remover('testing'))
        self.assertEqual('lx Stl', vowel_remover('Alex Steele'), 'Should be able remove upper and lower case vowels.')
        self.assertEqual('12345', vowel_remover('12345'))
        self.assertEqual('Dd y gt t t wrk?', vowel_remover('Did you get it to work?'),
                         'Should ignore non-alphanumeric values')


if __name__ == '__main__':
    unittest.main(failfast=True)
