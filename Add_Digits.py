def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    # while len(str(num)) != 1:
    #     num = sum([int(c) for c in str(num)])
    # return num

# Explain https://discuss.leetcode.com/topic/28791/3-methods-for-python-with-explains/8
    if num > 9:
        num = num%9
        if num == 0:
            num = 9
    return num


if __name__ == "__main__":
    num = 38
    print(addDigits(num))