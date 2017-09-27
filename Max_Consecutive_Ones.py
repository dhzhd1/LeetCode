def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = [x.count('1') for x in ''.join(str(nums)).split('0')]
    return max(count)


if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    print(str(findMaxConsecutiveOnes(nums)))