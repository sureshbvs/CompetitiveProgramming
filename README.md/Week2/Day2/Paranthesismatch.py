import unittest
def get_closing_paren(sentence, index):
    count = 0
    while index < len(sentence):
        char = sentence[index]
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
            if count is 0:
                return index
        index += 1
    if count!=0:
        raise Exception
# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)
