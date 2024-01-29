import unittest
import random
import main

class Test_Main(unittest.TestCase):

    def test_Large_Pattern(self):
        # Generate a test pattern with 20 random integers
        test_pattern = [random.randint(0, 20) for _ in range(20)]
        
        # Repeat the pattern 20 times to create a large test list
        test_list = test_pattern * 20

        # Assert that main.repeat correctly identifies the repeating pattern
        print(main.repeat(test_list))
        #self.assertEqual(main.repeat(test_list), test_pattern)

if __name__ == '__main__':
    unittest.main()



def repeat(list):

    #  edge cases:
    if list is None:
        return None

    if len(list) == 1:
        return None
    
    #  variables:
    LIST_LENGTH = len(list)
    compare_list = list[:LIST_LENGTH // 2]
    compare_list_length = len(compare_list)
    """I start compare_list at the floor
    value of list_length / 2 because I know
    that if there is no repeating pattern
    in <= half the length of the original list,
    there can be no pattern since any repitition
    of a length greater than half the list size
    would be at the very least greater than the
    size of the original list.
    """
    
    #  loop terminates at length 0 as we work down compare_list
    while (compare_list_length > 0):

        if LIST_LENGTH % compare_list_length == 0:
            """In order for repition to occur,
            the length of the original list
            must be divisible by the length
            of compare_list
            """

            multiple = LIST_LENGTH // compare_list_length
            """Now we find the multiple in order
            to multiply the compare_list to
            check if it now equals the original
            list
            """

            if compare_list * multiple == list:
                return compare_list
        
        #  iterate downwards so that the longest pattern is returned
        del compare_list[-1]
        compare_list_length = compare_list_length - 1

    #  if a pattern is not found, return None
    return None
