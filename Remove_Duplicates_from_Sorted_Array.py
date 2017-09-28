def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    index_end = len(nums)
    while i < index_end:
        if i + 1 < index_end and nums[i] == nums[i+1]:
            nums.pop(i)
            index_end -= 1
        else:
            i += 1
    print(i)
    return len(nums)

if __name__ == "__main__":
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
    print(nums)
