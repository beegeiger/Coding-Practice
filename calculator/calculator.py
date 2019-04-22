import operator
"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    ops1 = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.div}
    out = 0
    # print(s)
    # print(s[-5])
    # print('ops1 + = ' + str(ops1[(s[-5])]))
    out += (int(s[-3])) (ops1[(s[-5])]) (int(s[-1]))
    if len(s) > 5:
        output = output (ops1[(s[0])]) ((int(s[2])))
    return out
        


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
