# https://leetcode.com/problems/move-zeroes/
# easy

# this swap construst will be helpful
# i1, i2 = nums.index(a), nums.index(b)
# nums[i1], nums[i2] = nums[i2], nums[i1]


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    amount_zeros = nums.count(0)
    for i in range(amount_zeros):
        curr_zero_ind = nums.index(0)
        while curr_zero_ind < len(nums) - i - 1:
            if nums[curr_zero_ind + 1] != 0:
                nums[curr_zero_ind], nums[curr_zero_ind + 1] = nums[curr_zero_ind + 1], nums[curr_zero_ind]
            curr_zero_ind += 1
    
    return nums

def test():
    nums = [0, 1, 0, 3, 12]
    assert moveZeroes(nums) == [1, 3, 12, 0, 0]

    nums = [0]
    assert moveZeroes(nums) == [0]

    nums = [0, 0, 1]
    assert moveZeroes(nums) == [1, 0, 0]

if __name__ == '__main__':
    test()