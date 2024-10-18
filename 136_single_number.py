# https://leetcode.com/problems/single-number/ 

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # naive algo - not ok with time

    # help_arr = [0] * (len(nums))        

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             help_arr[i] = help_arr[j] = 1

    # ind = 0
    # for elem in help_arr:
    #     if elem == 0:
    #         break
    #     ind+=1
    # return nums[ind]


    # beautiful algo
    
    res = nums[0]
    for i in range(1, len(nums)):
        res ^= nums[i]
    
    return res
                     
             

def test():
    arr = [3, 2, 2, 3, 1]
    assert singleNumber(arr) == 1

if __name__ == '__main__':
    test()