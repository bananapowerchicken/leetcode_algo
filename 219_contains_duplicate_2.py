
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    count_dict = dict.fromkeys(set(nums), 0)

    # dict with repeated nums and their amount
    for n in nums:
        count_dict[n] += 1    
    print(count_dict)

    # no repeated
    print( count_dict, list(count_dict.values()).count(1), len(nums))
    
    if list(count_dict.values()).count(1) == len(nums):
        return False

    for el in count_dict:
        num, amount = el, count_dict[el]
        if amount > 1:
            # lists of repeating indicies
            indicies = get_indices(el, nums)
            print(indicies)
            if get_deltas(indicies, k):
                return True
    
    return False
        


def get_indices(element, lst):
    return [i for i in range(len(lst)) if lst[i] == element]

def get_deltas(indicies_list, k):
    for i in range(len(indicies_list)):
        j = i + 1
        while j < len(indicies_list):
            if abs(indicies_list[i] - indicies_list[j]) <= k:
                return True
            j += 1
    
    return False





def test():

    nums = [1]
    k = 1
    assert containsNearbyDuplicate(nums, k) == False

    nums = [1, 2, 3, 1]
    k = 3
    print('res = ', containsNearbyDuplicate(nums, k))
    assert containsNearbyDuplicate(nums, k) == True

    nums = [1, 0, 1, 1]
    k = 1
    assert containsNearbyDuplicate(nums, k) == True

    nums = [1,4,2,3,1,2]
    k = 3
    assert containsNearbyDuplicate(nums, k) == True





if __name__ == '__main__':
    test()