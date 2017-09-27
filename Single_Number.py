def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    result = set(nums[::2]) - set(nums[1::2])
    return list(result)[0]

if __name__ == "__main__":
    nums = [1,2,3,1,3,2,5,6,7,5,6]
    print(str(singleNumber(nums)))



