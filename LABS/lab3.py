"""
UTM: CSC108, Fall 2025

Practical Lab 3

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
You may not use any "if" statements or loops of any kind within this lab.
This is because they have not been fully introduced yet in class, and we would
like you to use the string methods that you have already learned to complete
this lab. Also, please do not TRY to use try-except, we'll 'catch' it ;)

You have been warned!
"""


def exists_triangle(x: float, y: float, z: float) -> bool:
    """
    Place your "exists_triangle" function from last lab here.

    The same restrictions as last week will apply.

    Please remember to write doctests, you must write them below this line:
    >>> exists_triangle(1.0, 1.0, 1.0)
    True
    >>> exists_triangle(1.0, 1.0, 0.0)
    False
    >>> exists_triangle(1.0, -1.0, 0.0)
    False
    """
    return (x + y > z) and (y + z > x) and (z + x > y)


def is_triangle_string(string: str) -> bool:
    """
    Given an input in the form of some string that looks like "111222333",
    return True if <string> is a triangle string, False otherwise.

    For the purposes of this function, we define a triangle string as a string
    which could represent a proper triangle if its characters were converted
    into the sides of a triangle. What we mean by this is, if let's say the
    three distinct characters within the string each represented one side of
    the triangle, and the number of occurrences of each distinct character
    represented the length of that side, and those three sides could form a
    proper triangle as defined in lab 2, then <string> is a triangle string.

    Precondition: <string> will be a string with three distinct characters,
                  and there will be exactly two positions within the string
                  where adjacent characters differ (are different). The length
                  of <string> will always be >= 3. Note that the characters do
                  not have to be 1, 2 and 3 like the example given above, they
                  could be any printable character.

    Restrictions: you must use your "exists_triangle" function from lab 2 as a
                  helper for this function, in addition to the lab restrictions
                  defined at the start of this file. You are allowed and are
                  encouraged to fix any issues with your previous submission
                  for this function. More explicitly, this means that somewhere
                  within the body of this function, there must be a function
                  call to the "exists_triangle" function defined above.

    Please remember to write doctests, you must write them below this line:
    >>> is_triangle_string("112222333")
    True
    >>> is_triangle_string("1122334")
    False
    >>> is_triangle_string("111223")
    False
    """
    a = string.count(string[0])
    b = string.count(string[a])
    c = string.count(string[a + b])

    return len(string) == a + b + c and exists_triangle(a, b, c)


def is_palindrome(string: str) -> bool:
    """
    Given <string>, return True if it is a palindrome and False otherwise.

    For the purposes of this function, we consider a string a palindrome if
    the letters (ignoring spaces and capitalization) are the same going from
    left to right and from right to left.

    Some examples, "Racecar" is a palindrome, and so is "ab ba". "abc" is not
    a palindrome.

    Precondition: <string> will not be empty and the only non-alphanumeric
                  English characters in <string> will be whitespace.

    Please remember to write doctests, you must write them below this line:
    >>> is_palindrome("Racecar")
    True
    >>> is_palindrome("Shayan")
    False
    >>> is_palindrome("a")
    True
    """
    reverse_string = string[::-1]
    return reverse_string.lower() == string.lower()


def is_triple_string(string: str) -> bool:
    """
    This function is a little similar to the triangle string function above,
    if you feel like you can reuse some of the code you wrote for that function
    here, feel free to do so.

    Given <string>, return True if it is a triple string and False otherwise.

    For the purposes of this function, we define a triple string as any string
    that is made up of some substring repeating exactly three times.
    For the MAT102 folks out there, that is, any combination of characters C
    such that there exists a substring c of C and C = c+c+c.

    For example, the string "111" is a triple string, which consists of "1"
    repeated three times. "111111" is also a triple string, which consists of
    "11" repeated three times.

    Please remember to write doctests, you must write them below this line:
    >>> is_triple_string("222")
    True
    >>> is_triple_string("2222")
    False
    >>> is_triple_string("ababab")
    True
    """
    return (
        len(string) % 3 == 0
        and string[0:int(len(string) / 3)] * 3 == string
    )
