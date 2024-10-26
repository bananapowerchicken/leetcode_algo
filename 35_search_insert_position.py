# https://leetcode.com/problems/search-insert-position
# easy

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target <= nums[0]:
        return 0
    
    if target > nums[-1]:
        return len(nums)
    
    if target == nums[-1]:
        return len(nums) - 1
    
    for i in range(1, len(nums)):
        if target <= nums[i]:
            return i
    
    return len(nums)

        


def test():
    nums = [1,3]
    target = 3
    assert searchInsert(nums, target) == 1


if __name__ == '__main__':
    test()