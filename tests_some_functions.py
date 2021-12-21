import unittest
import some_functions

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,3)), 6, "Should be 6")

class TestMyFunctions(unittest.TestCase):
    
    def test_hello_name_f(self):
        self.assertEqual(some_functions.hello_name_f('Tomek'), 'Hello Tomek!', "Should be Hello Tomek")


if __name__ == '__main__':
    unittest.main()
