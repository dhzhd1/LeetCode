def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    nums.sort()
    count = nums.count(val)
    if count > 0:
        index = nums.index(val)
        for _ in xrange(count):
            nums.pop(index)

    return len(nums)




if __name__ == "__main__":
    nums = [3,2,2,3,2]
    val = 3
    count = removeElement(nums, val)
    print(count)
    print(nums)

    nums = []
    val = 0
    count = removeElement(nums, val)
    print(count)
    print(nums)