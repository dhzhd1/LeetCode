def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr = sorted(nums, key=int)
    return sum(arr[::2])



if __name__ == "__main__":
    nums = [1,4, 2, 3]
    print(str(arrayPairSum(nums)))


