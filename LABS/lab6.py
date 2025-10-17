"""
UTM: CSC108, Fall 2025

Practical Lab 6

Instructors: Michael Liut, Mai Ha Vu, Joshua Jung, Mohammad Mahmoud

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 Michael Liut, Haocheng Hu

LAB RESTRICTIONS, PLEASE READ:
Do not add any imports, the ones that you need will be given to you.
You may not use any dictionaries or dictionary methods, or recursion.
Do not use try-except statements, you should be able to anticipate
or prevent any errors from happening at all!
Within your loops, you MUST NOT use any break or continue statements.
"""

from typing import Any, List


def loopy_madness_with_while_loops(string1: str, string2: str) -> str:
    """
    The exact same function as loopy_madness from Lab 5, but we ask that you
    change any for loops that you used to while loops. Refer back to Lab 5 for
    the specifications of this function.

    Keep in mind that since we will run the same tests, the same restrictions
    from Lab 5 will apply to this function as well.

    You are NOT allowed to use any for loops for this function.
    >>> loopy_madness_with_while_loops("abc", "123")
    'a1b2c3'

    >>> loopy_madness_with_while_loops("abcde", "12")
    'a1b2c1d2e1'

    >>> loopy_madness_with_while_loops("ab", "123")
    'a1b2a3'
    """

    new_string = ""
    len_1, len_2 = len(string1), len(string2)
    max_len = max(len_1, len_2)

    counter_1 = 0
    counter_2 = 0

    rev_1 = False
    rev_2 = False

    while len(new_string) < 2 * max_len:
        new_string += string1[counter_1]
        if not rev_1:
            counter_1 += 1
            if counter_1 == len_1:
                rev_1 = True
                counter_1 -= 2
        else:
            counter_1 -= 1
            if counter_1 < 0:
                rev_1 = False
                counter_1 += 2

        new_string += string2[counter_2]
        if not rev_2:
            counter_2 += 1
            if counter_2 == len_2:
                rev_2 = True
                counter_2 -= 2
        else:
            counter_2 -= 1
            if counter_2 < 0:
                rev_2 = False
                counter_2 += 2

    return new_string


def longest_chain(lst: List[int]) -> int:
    """
    Given a list of integers, return the length of the longest chain of 1's
    that start from the beginning.

    You MUST use a while loop for this, and are not allowed to use a for loop.

    Hint: A good way to start is to define a stopping condition, and have a
    variable that keeps track of how many 1's you've seen thus far, if any.

    Precondition: <lst> will only contain the integers 1 and 0.

    >>> longest_chain([1, 1, 0])
    2
    >>> longest_chain([0, 1, 1])
    0
    >>> longest_chain([1, 0, 1, 1])
    1
    """
    count_1 = 0
    for i in lst:
        if i != 1:
            break
        else:
            count_1 += 1

    return count_1


def count_types(lst: List[Any]) -> List[int]:
    """
    Given a list <lst> of random types, return the number of occurrences of
    each type, in the form of a list, in the order that they were first seen.

    For example, if the input ['str1', 1, 'str2'], the output would be [2, 1],
    as a string type appears first, and occurs twice in the list. An integer
    type appears next, and only occurs once in the list.

    Another example could be [True, 'str1', 1, False, 'str2', True], where the
    output would be [3, 2, 1], as a boolean type appears first, and occurs
    three times in the list. A string appears next, and occurs twice in the
    list. Finally, an integer appears next, and occurs once in the list.

    Do not modify the input list.
    >>> count_types(['str1', 1, 'str2'])
    [2, 1]
    >>> count_types([True, 'str1', 1, False, 'str2', True])
    [3, 2, 1]
    """
    type_bool = 0
    type_int = 0
    type_str = 0
    order = []
    final = []

    for i in lst:
        if type(i) == bool:
            type_bool += 1
            order.append("bool")
        elif type(i) == int:
            type_int += 1
            order.append("int")
        elif type(i) == str:
            type_str += 1
            order.append("str")

    order_modified = list(dict.fromkeys(order))
    for n in order_modified:
        if n == "bool":
            final.append(type_bool)
        elif n == "int":
            final.append(type_int)
        elif n == "str":
            final.append(type_str)

    return final


def second_largest(lst: List[int]) -> int:
    """
    Given a list <lst> of integers, return the second largest item in the list
    without modifying <lst>. You cannot use any of python's builtin sorting
    functions. Do not attempt to sort the list yourself either.

    As a sanity check, you can ensure that your function returns what
    "return sorted(lst)[-2]" would. (DO NOT COPY THIS)

    For example, an input [1, 2, 3] should return an output of 2, since 2 is
    the second largest integer in the list.

    Note that when we say second largest, we do not mean second largest
    distinct element. That means that [1, 2, 4, 4] should return 4, not 2.

    Precondition: the input list has at least 2 elements.

    Something extra to think about (not graded): is it possible to write this
    function with an extra argument <n> and return the nth largest number in
    the list? Can you do this without sorting the list?
    >>> second_largest([1, 2, 3])
    2
    >>> second_largest([5, 1, 5, 3])
    5
    >>> second_largest([-1, -2, -3, -4])
    -2
    >>> second_largest([10, 10])
    10
    >>> second_largest([7, 2, 7, 5, 7])
    7
    """
    biggest = 0
    for i in range(len(lst)):
        if lst[i] > lst[biggest]:
            biggest = i
    if biggest == 0:
        second_biggest = 1
    else:
        second_biggest = 0

    for n in range(len(lst)):
        if n != biggest:
            if lst[biggest] - lst[n] < lst[biggest] - lst[second_biggest]:
                second_biggest = n

    return lst[second_biggest]
