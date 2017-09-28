def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    return a if b == 0 else getSum((a ^ b), (a & b) << 1)

if __name__ == "__main__":
    a = 1
    b = 2
    print(getSum(a, b))