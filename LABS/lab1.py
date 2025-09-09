"""
UTM: CSC108, Fall 2025

Practical Lab 1

Instructors: Michael Liut, Mai Ha Vu, Joshua Jung, Mohammad Mahmoud

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 Michael Liut, Haocheng Hu

WARNING: Do not modify the comments or variable names in this file, our tests
are looking for specific variables and comments, modifying them could result in
loss of marks.
"""

# complete the following exercises below

# TODO
# Q1
a = 1
b = 2
# without changing the values of a and b,
# declare a variable 'c' and make it equal to the value of a + b
c = a + b

# TODO
# Q2
# We are going to play with something called floor division
# Say you had 15 cookies to distribute to 4 children and you had to give the
# same number of cookies to each child, how many cookies could you afford
# to give each child?
num_cookies = 15
num_children = 4
# Use the floor division operator "//" to calculate this number
cookies_to_give_each_child = 15//4

# Q3
# Go learn about a cool thing that you can do with just python and numbers
# explain it in a comment and show a demonstration below:

# TODO
# comments go here
#
# When you floor divide a negative with a positive the answer actually always goes down, for example I said that
# -1//3 = -1 but 1//3 equals 0. This is because floor division always rounds towards negative infinity.
#
# TODO
# Give a demonstration of actual WORKING code below this line

x = -1//3
y = 1//3
