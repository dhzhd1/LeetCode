def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    if n % 4 == 0:
        return False
    else:
        return True




if __name__ == "__main__":
    n = 4
    print(canWinNim(n))

    n = 5
    print(canWinNim(n))
