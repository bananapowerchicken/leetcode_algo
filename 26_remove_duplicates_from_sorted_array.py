# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# easy
# arrays

# complexity 
# time: O(n) - once go through list 
# space O(1) - only vars


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 1
    el = nums[0]
    for n in nums:
        if n != el:
            el = n
            nums[k] = el
            k += 1
    
    return k



def test():
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert removeDuplicates(nums) == 5


if __name__ == '__main__':
    test()