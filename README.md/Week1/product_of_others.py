"""
def product(arr,i):
    arr.remove(arr[i])
    product=1
    for i in range(len(arr)):
        product=product*arr[i]
    return product
l=[int(q) for q in input().split()]
x=[]
x=l[:]
l2=[]
for i in range(len(x)):
    x1=product(l,i)
    l2.append(x1)
    l=x[:]
print(l2)    
"""
import unittest


def get_products_of_all_ints_except_at_index(array):
    if len(array) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')
    productExceptIndex = [None] * len(array)
    product= 1
    for i in xrange(len(array)):
        productExceptIndex[i] = product
        product *= array[i]
    product = 1
    for i in xrange(len(array) - 1, -1, -1):
        productExceptIndex[i] *= product
        product *= array[i]

    return productExceptIndex




# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)