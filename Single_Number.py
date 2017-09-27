def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    i = 0
    while i < len(nums):
        if i+1 > len(nums) or (nums[i] not in nums[i+1:]):
            return nums[i]
        i += 2

if __name__ == "__main__":
    nums = [1,2,3,1,3,2,5,6,7,5,6]
    print(str(singleNumber(nums)))



