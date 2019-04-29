"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""
    hex_val = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    counter = 0
    hex_in = hex_in[::-1]
    for dig in range(0, len(hex_in)):
        d = hex_in[dig]
        if d.isdigit():
            counter += int(d) * (16 ** dig)
        else:
            counter += hex_val[d] * (16 ** dig)
    return counter


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")
