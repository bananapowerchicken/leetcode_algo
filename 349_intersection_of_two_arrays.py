# https://leetcode.com/problems/intersection-of-two-arrays/
# easy

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # nums1.sort()
    # nums2.sort()
    # set1 = set(nums1)
    # set2 = set(nums2)
    # res = set1.intersection(set2)
    # # print('res = ', list(res))
    # return list(res) 

    return list(set(nums1).intersection(set(nums2)))


def test():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    assert intersection(nums1, nums2) == [9, 4]


if __name__ == '__main__':
    test() 