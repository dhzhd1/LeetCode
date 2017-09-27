def findLUSlength(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    if a != b:
        return max(len(a), len(b))
    else:
        return -1




if __name__ == "__main__":
    a = "aba"
    b = "cdc"
    print(findLUSlength(a, b))
    a = "aefawfawfawfaw"
    b = "aefawfeawfwafwaef"
    print(findLUSlength(a, b))