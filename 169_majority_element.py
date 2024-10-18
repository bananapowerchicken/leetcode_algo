# https://leetcode.com/problems/majority-element
# easy


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    if n == 0:
        raise ValueError("Input list is empty")

    if n < 3:
        return nums[0]
    
    count_dict = {}

    for num in nums:
        if num not in count_dict.keys():
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    
    return max(zip(count_dict.values(), count_dict.keys()))[1]
        

def test():
    nums = [2,1,1,1,1,2,2]
    assert majorityElement(nums) == 1

if __name__ == '__main__':
    test()

# may duplicate
# always exists the major num - so is it unique? must be
# major appears more than n/2 times (n - len nums)
