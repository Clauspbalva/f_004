"""
p_004.py | Claus Pagano | Last update: 2022-8-22

Algorithms and Data Structures practice with Python

"""

# --------------------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------------------

from .f_000 import function_test


# --------------------------------------------------------------------------------------------------
# FUNCTION DECLARATION 
# --------------------------------------------------------------------------------------------------

def substractions(n1, n2):
    """
        Description: returns the division of n1 and n2 by Euclid's algorithm

        Parameters:
            n1 (int): number 1
            n2 (int): number 2

        Return:
            mcd (int) = n1 / n2
    """

    # Validates parameters: integer type
    if type(n1) != int or type(n2) != int:
        return 'ERROR'

    # Determines result sign
    if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
        sign = 1
    else:
        sign = -1
    n1 = abs(n1)
    n2 = abs(n2)

    # Greatest common divisor
    mcd = 0  
    if n1 != 0 or n2 != 0:  
        while n1 >= n2:
            n1 = n1 - n2
            mcd += 1
        return (mcd, n1)


# --------------------------------------------------------------------------------------------------
# TESTING
# --------------------------------------------------------------------------------------------------

# Dictionary with test cases 
test_config = {
    'function': substractions,
    'input_names': ['n1', 'n2'],
    'num_precision': [0.5],
    'tests': [
        {'id': 1, 'input_values': [None, None], 'output_expected': None},
        {'id': 2, 'input_values': [-1, 3], 'output_expected': -0.33},
        {'id': 3, 'input_values': [10, 5], 'output_expected': 2},
        {'id': 4, 'input_values': [0.1, 3], 'output_expected': None},
        {'id': 5, 'input_values': [18, 2], 'output_expected': 9}
    ],
    'print_details': True  
}



# --------------------------------------------------------------------------------------------------
# MAIN PROCEDURE
# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":
   function_test(test_config)


    