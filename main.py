def repeat(input_list):

    #  edge cases:
    if input_list is None:
        return None

    if len(input_list) == 1:
        return None
    
    #  variables:
    list_length = len(input_list)
    compare_list = input_list[:list_length // 2]
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

        if list_length % compare_list_length == 0:
            """In order for repition to occur,
            the length of the original list
            must be divisible by the length
            of compare_list
            """

            multiple = list_length // compare_list_length
            """Now we find the multiple in order
            to multiply the compare_list to
            check if it then equals the original
            list
            """

            if compare_list * multiple == input_list:
                return compare_list
        
        #  iterate downwards so that the longest pattern is returned
        del compare_list[-1]
        compare_list_length = compare_list_length - 1

    #  if a pattern is not found, return None
    return None
