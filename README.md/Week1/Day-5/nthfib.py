import unittest
def fibonacci(n):
    count = 1
    a,b = 0,1
    fib = 0
    while n != count:
        fib = a + b
        count = count+1
        a,b = b,fib
    return fib

def fib(n):
    # Compute the nth Fibonacci number
    if n < 0:
        raise IndexError("can't find")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
       x= fibonacci(n)
    return x
# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)
