def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for num in findNums:
        large_list = [x for x in nums[nums.index(num):] if x > num]
        if len(large_list) == 0:
            result.append(-1)
        else:
            result.append(large_list[0])
    return result

if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(nextGreaterElement(nums1, nums2))