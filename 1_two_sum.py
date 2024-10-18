# https://leetcode.com/problems/two-sum/
# from math import abs

def twoSum(nums: list, target: int) -> list:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 2:
        return [0, 1]
    for i in range(0, len(nums)):
        # if abs(nums[i]) > abs(target):
        #     continue
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
        

def test():
    # nums = [2, 7, 11, 15]
    # target = 9
    # assert twoSum(nums, target) == [0, 1]

    # nums = [7, 11]
    # target = 18
    # assert twoSum(nums, target) == [0, 1]

    nums = [7, -3, -2]
    target = -5
    assert twoSum(nums, target) == [1, 2]

if __name__ == '__main__':
    test()