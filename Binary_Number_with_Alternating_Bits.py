# coding=utf-8

"""
Given a positive integer, check whether it has alternating bits:
namely, if two adjacent bits will always have different values.
"""


def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    result = True
    if n != 0:
        last_bit = 1 & n
        n = n >> 1
        while n != 0 and result is True:
            if last_bit ^ (1 & n) == 1:
                last_bit = 1 & n
                n = n >> 1
            else:
                result = False
    return result


if __name__ == "__main__":
    num = [5, 7,11, 10]
    for i in num:
        print(hasAlternatingBits(i))