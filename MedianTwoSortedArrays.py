def findMedianSortedArrays(nums1, nums2):
    combine_list = sorted(nums1 + nums2, key=int)
    if len(combine_list) % 2 == 0:
        return 0.5 * (combine_list[len(combine_list) / 2] + combine_list[len(combine_list) / 2 - 1])
    else:
        return 1. * combine_list[int(len(combine_list) / 2)]

if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    median_value = findMedianSortedArrays(nums1, nums2)
    print(median_value)