# https://leetcode.com/problems/move-zeroes/
# easy

# moving from the end to avoid neighbour nulls


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = -1 # curr index
    next_zero_end_ind = -1 # ind to put next zero to the end
    len_negative = -len(nums)

    while i >= len_negative: # process [0] case
        if nums[i] == 0:
            next_i = i - 1
            next_zero_end_ind = swap_to_end(nums, i, next_zero_end_ind)
            if next_i < len_negative:
                break
            i = next_i
        else:
            i -= 1
    
    return nums


def swap_to_end(nums, i, next_zero_end_ind):   
    while i != next_zero_end_ind:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        i += 1
    return i-1


def test():
    nums = [0, 1, 0, 3, 12]
    assert moveZeroes(nums) == [1, 3, 12, 0, 0]


if __name__ == '__main__':
    test()