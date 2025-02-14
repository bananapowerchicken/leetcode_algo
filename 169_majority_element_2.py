# https://leetcode.com/problems/majority-element
# easy
# arrays
# the best - space O(1) - Boyer Moore vooting: candidate

# complexity nice decision
# time: O(n) * 3 - once go through the array (every element)
# space O(n) - set gives O(n)


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    threshold = len(nums) / 2
    el_amounts = {x: 0 for x in set(nums)} # set O(n), create dict O(n) - time

    # through array O(n) - time
    for el in nums:
        el_amounts[el] += 1
        if el_amounts[el] > threshold:
            return el

        

def test():
    nums = [2,1,1,1,1,2,2]
    assert majorityElement(nums) == 1

    nums = [3,2,3]
    assert majorityElement(nums) == 3

    nums = [2,2,1,1,1,2,2]
    assert majorityElement(nums) == 2

if __name__ == '__main__':
    test()

