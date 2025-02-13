# https://leetcode.com/problems/move-zeroes/
# easy

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = -1
    next_zero_ind = -1 # ind to put next zero - should be shifted
    len_minus = -len(nums)

    while i >= len_minus: # process [0] case
        if nums[i] == 0:
            next_i = i - 1
            next_zero_ind = swap_to_end(nums, i, next_zero_ind)
            # next_zero_ind -= 1
            if next_i < len_minus:
                break
            i = next_i
        else:
            i -= 1
    
    return nums


def swap_to_end(nums, i, next_zero_ind):   
    while i != next_zero_ind:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        i += 1
    i -= 1
    return i


def test():
    nums = [0, 1, 0, 3, 12]
    assert moveZeroes(nums) == [1, 3, 12, 0, 0]


if __name__ == '__main__':
    test()