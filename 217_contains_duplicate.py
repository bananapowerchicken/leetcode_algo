# https://leetcode.com/problems/contains-duplicate
# easy

def revcontainsDuplicateerse(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(set(nums)) < len(nums)


def test():
    nums = [1,2,3,1]
    assert revcontainsDuplicateerse(nums) == True


if __name__ == '__main__':
    test()