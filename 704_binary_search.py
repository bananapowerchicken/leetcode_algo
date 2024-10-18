# https://leetcode.com/problems/binary-search/
# complexity: log2(n), n - list len
# searching by the middle

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1    

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1        

    return -1

def test():
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 3
    assert binary_search(nums, target) == 2

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert binary_search(nums, target) == 4

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert binary_search(nums, target) == -1

if __name__ == '__main__':
    test()