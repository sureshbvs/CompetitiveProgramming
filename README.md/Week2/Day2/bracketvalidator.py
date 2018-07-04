import unittest
def isMatchingPair(char1,char2):
       if char1 == '(' and  char2 == ')':
         return True
       if char1 == '{' and char2 == '}':
         return True
       if char1 == '[' and char2 == ']':
         return True
       else:
         return False
def is_valid(char):
       stack=[]
       for i in range(len(char)):
          if char[i] == char[i] == '{' or char[i] == '(' or char[i] == '[':
              stack.append(char[i])
          if char[i] == '}' or char[i] == ')' or char[i] == ']':
              if not stack:
                   return False
              elif isMatchingPair(stack.pop(), char[i]) ==False:
                  return False
       if not stack:
           return True
       else:
           return False
# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
