import unittest
import random
import main

class Test_Main(unittest.TestCase):

    def test_Empty_Input(self):
        self.assertEqual(main.repeat(), None)
    
    def test_One_Element_Input(self):
        self.assertEqual(main.repeat([1]), None)

    def test_Empty_List(self):
        self.assertEqual(main.repeat([]), None)
    
    def test_String_Input(self):
        self.assertEqual(main.repeat("HelloHello"), "Hello")

    def test_Large_Pattern(self):
        # Generate a test pattern with 20 random integers
        test_pattern = [random.randint(0, 20) for _ in range(20)]
        
        # Repeat the pattern 20 times to create a large test list
        test_list = test_pattern * 20

        # Assert that main.repeat correctly identifies the repeating pattern
        self.assertEqual(main.repeat(test_list), test_pattern * 10)

if __name__ == '__main__':
    unittest.main()
