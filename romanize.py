#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""Simple command-line tool to convert an Arabic numeral between 1 & 3999 to its Roman form.

Usage:
  $ python romanize.py 234
  Roman numeral for 234 is - CCXXXIV
  $
"""

__author__ = 'me@phalgun.in (Phalgun Guduthur)'

import sys

'''
    The core algorithm to print roman numerals, based on the patterns in them.
    1 to 5:
        I
        II
        III
          IV
           V

    6 to 10:
        VI
        VII
        VIII
           IX
            X

    101 to 105:
        CI
        CII
        CIII
        C  IV
        C   V

    We see a pattern for every set of 5 numbers. Each number has a lower bound, repetition character and upper bound
    and every number follows the patter.

'''
def pattern_print(n, lower, r, upper): # r is the repetition character
    if n == 0:
        return '' # This case is highly unlikely as 0 is handled in the ancestor method
    elif n == 1:
        return lower + r
    elif n == 2:
        return lower + r + r
    elif n == 3:
        return lower + r + r + r
    elif n == 4:
        return r + upper
    elif n == 5:
        return upper

'''
    This method prints the pattern. Based on whether the number is less than or more than 5,
    it specifies the bounds for the pattern.
'''
def roman_string_for_digit(n, one, five, ten):
    if int(n) <= 5:
        return pattern_print(int(n), '', one, five)
    else:
        return pattern_print(int(n) - 5, five, one, ten)

'''
    This method decides if the number belongs to the units, tens, hundreds or thousands
    range and then calls the pattern method by giving the one, five and ten roman characters
'''
def romanize(n):
    first_digit = str(n)[0]
    if int(first_digit) == 0:
        return ''
    if n <= 9:
        return roman_string_for_digit(first_digit, 'I', 'V', 'X')
    elif n <= 99:
        return roman_string_for_digit(first_digit, 'X', 'L', 'C')
    elif n <= 999:
        return roman_string_for_digit(first_digit, 'C', 'D', 'M')
    elif n <= 3999:
        return roman_string_for_digit(first_digit, 'M', '', '')

'''
    This method reverses the number supplied and prints the roman equivalent of each number.
    The `multiplier` is used to maintain the units, tens, hundreds and thousands value.

    Once the equivalent roman value is obtained, this value is prefixed to the existing roman equivalent.
    Once the loop is done, the `roman_numeral` contains the final roman form of `num`
'''
def get_roman_equivalent(num):
    roman_numeral = ''
    multiplier = 1

    reversed_number = str(num)[::-1] # reverses the number
    for x in reversed_number: # loop through the reversed number
        roman_numeral = str(romanize(int(x) * multiplier)) + roman_numeral # prefix the new value

        multiplier = multiplier * 10 # iterate the multiplier too

    # Done, return
    return roman_numeral

'''
    Method to sanitize inputs
'''
def valid_input(arg_list):
    if len(arg_list) != 2:
        return False

    number = int(arg_list[1])
    if not number or number < 1 or number > 3999:
        return False

    return True

if __name__ == "__main__":
    if not valid_input(sys.argv):
        print 'Invalid usage. $python romanize.py <number between 1 & 3999>'
    else:
        roman_form = get_roman_equivalent(sys.argv[1])

        print 'Roman numeral for ' + str(sys.argv[1]) + ' is - ' + str(roman_form)


