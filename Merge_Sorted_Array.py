def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    for i in xrange(n):
        nums1[m + i] = nums2[i]
    nums1.sort()


if __name__ == "__main__":
    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1
    # merge(nums1, m, nums2, n)
    # print nums1

    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)