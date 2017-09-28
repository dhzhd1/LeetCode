def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    cursor = 0
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[cursor] = nums[cursor], nums[i]
            cursor += 1

if __name__ == "__main__":
    nums = [0, 0, 0, 1, 0, 3, 12,0 ,0]
    moveZeroes(nums)
    print(nums)
