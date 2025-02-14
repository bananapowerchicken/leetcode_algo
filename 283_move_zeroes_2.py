# https://leetcode.com/problems/move-zeroes/
# easy

# moving from the end to avoid neighbour nulls

# fix place where should be next nonzero element moved!!!! this way only one cycle is required

# complexity nice decision
# time: O(n) - once go through the array (every element)
# space O(1) - almost no extra memory

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # crap

    # i = -1 # curr index
    # next_zero_end_ind = -1 # ind to put next zero to the end
    # len_negative = -len(nums)

    # while i >= len_negative: # process [0] case
    #     if nums[i] == 0:
    #         next_i = i - 1
    #         next_zero_end_ind = swap_to_end(nums, i, next_zero_end_ind)
    #         if next_i < len_negative:
    #             break
    #         i = next_i
    #     else:
    #         i -= 1

    # nice decision
    # may add check if indexes are  already equal - but don't know, what is faster
    next_nonzero_elem_ind = 0
    i = 0
    
    while i < len(nums):
        if nums[i] != 0:
            nums[next_nonzero_elem_ind], nums[i] = nums[i], nums[next_nonzero_elem_ind]
            next_nonzero_elem_ind +=1
        i += 1



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