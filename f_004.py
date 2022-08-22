"""
p_004.py | Claus Pagano | Last update: 2021-11-8

Algorithms and Data Structures practice with Python

"""

def substractions(n1, n2):
    """
        Description: returns the division of n1 and n2 by Euclid's algorithm

        Parameters:
            n1 (int): number 1
            n2 (int): number 2

        Return:
            n3 (int) = n1 / n2
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

    mcd = 0  
    if n1 != 0 or n2 != 0:  
        while n1 >= n2:
            n1 = n1 - n2
            mcd += 1
        return (mcd, n1)

# --------------------------------------------------------------------------------------------------
# TESTING
# --------------------------------------------------------------------------------------------------

def test():
    """
        Description: tests multiply function

        Parameters: none
    """

    test_params = [
        {'n1': 10, 'n2': 5},
        {'n1': 1, 'n2': '12'},
        {'n1': 0, 'n2': 0},
        {'n1': 0, 'n2': 1},
        {'n1': 0, 'n2': -1},
        {'n1': 1, 'n2': 0},
        {'n1': -1, 'n2': 0},
        {'n1': 1, 'n2': 1},
        {'n1': 1, 'n2': -1},
        {'n1': 2, 'n2': 8},
        {'n1': -2, 'n2': 8},
        {'n1': -2, 'n2': -8},
        {'n1': 10, 'n2': 20},
        {'n1': 2, 'n2': -3}
    ]

    print('\n')
    print('---------------------------------------------------------')
    print('Test ID |  n1  |  n2  | Result | Expected Result | Status')
    print('---------------------------------------------------------')
    for i, params in enumerate(test_params):
        r = substractions(params['n1'], params['n2'])
        if type(params['n1']) == int and type(params['n2']) == int:
            er = params['n1'] / params['n2']
        else:
            er = 'ERROR'
        status = 'OK' if r == er else 'NOK'
        print(f'{i : ^7} | {params["n1"] : >4} | {params["n2"] : >4} | {r : >6} | {er : >15} | {status : ^6}')


# --------------------------------------------------------------------------------------------------
# MAIN PROCEDURE
# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":
   test()


    