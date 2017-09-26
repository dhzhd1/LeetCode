def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    flat_list = []
    for elem_list in nums:
        for elem in elem_list:
            flat_list.append(elem)

    result_list = []
    if r * c > len(flat_list):
        return nums
    else:
        for i in xrange(r):
            result_list.append(flat_list[i * len(flat_list) / r: (i + 1) * len(flat_list) / r])

    return result_list


if __name__ == "__main__":
    nums = [[1,2], [3,4]]
    r = 1
    c = 4
    print(matrixReshape(nums, r, c))
    r = 2
    c = 4
    print(matrixReshape(nums, r, c))
    nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
    r = 42
    c = 5
    print(matrixReshape(nums, r, c))
    nums = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]]
    r = 22
    c = 15
    print(matrixReshape(nums, r, c))