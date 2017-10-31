# coding=utf-8

"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""


def reverseBits(n):
    """
    :param n: integer
    :return:  an integer
    """
    s = bin(n)
    result = n
    for i in xrange(0, 16):
        if n >> i & 1 ^ 1 == n >> (31-i) & 1 ^ 1:
            continue
        else:
            if n >> i & 1 ^ 1 == 1:
                result = result & ~(1 << (31-i))
                result = result | (1 << i)
            else:
                result = result | (1 << (31 -i))
                result = result & ~(1 << i)
    return result


if __name__ == "__main__":
    num = 43261596
    assert  reverseBits(num) == 964176192
    print(reverseBits(num))
