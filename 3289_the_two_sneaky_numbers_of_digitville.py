# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

def getSneakyNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    num_amount = len(nums) - 2
    counter_arr = [0] * num_amount
    res = []

    for i in range(len(nums)):
        counter_arr[nums[i]]+=1
    
    print(counter_arr)
    
    for i in range(len(counter_arr)):
        if counter_arr[i] == 2:
            res.append(i)
    
    print(res)
    return res

                     
             

def test():
    arr = [3, 2, 2, 3, 1, 0]
    assert getSneakyNumbers(arr) == [2, 3]

    arr = [0,1,1,0]
    assert getSneakyNumbers(arr) == [0, 1]

    arr = [0,3,2,1,3,2]
    assert getSneakyNumbers(arr) == [2, 3]

    arr = [7,1,5,4,3,4,6,0,9,5,8,2]
    assert getSneakyNumbers(arr) == [4, 5]

if __name__ == '__main__':
    test()