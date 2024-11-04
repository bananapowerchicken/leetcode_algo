
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    count_dict = dict.fromkeys(set(nums), 0)

    for n in nums:
        count_dict[n] += 1
    
    print(count_dict)

    for el in count_dict:
        num, amount = el, count_dict[el]
        if amount > 1:
            indicies = get_indices(el, nums)
            print(indicies)
            # for i in range(amount):
            #     i_min = nums.index(num)
            #     i_max = nums.index(num, i + 1) # need to add reversing the list and count from end
            # print(abs(i - j), k)
            # if abs(i - j) <= k:
            #     return True
    
    return False

def get_indices(element, lst):
    return [i for i in range(len(lst)) if lst[i] == element]

def get_deltas(indicies_list):
    




def test():
    nums = [1,0,1,1]
    k = 1
    assert containsNearbyDuplicate(nums, k) == True



if __name__ == '__main__':
    test()