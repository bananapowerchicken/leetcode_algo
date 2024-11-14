# https://leetcode.com/problems/group-anagrams/
# medium


# check if anagram s1, s2
# group properly

def isAnagram(s1, s2):
    r1 = ''.join(sorted(s1))
    r2 = ''.join(sorted(s2))
    return r1 == r2


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res_list = []    
    curr_anagrams_list = [strs.pop(0)]

    while len(strs):        
        for s in strs:
            print(s)
            if isAnagram(s, curr_anagrams_list[-1]):
                curr_anagrams_list.append(s)
        
        for el in curr_anagrams_list:
            if el in strs:
                strs.pop(strs.index(el))
        
        
        if len(strs) > 0:
            res_list.append(curr_anagrams_list)
            curr_anagrams_list = [strs.pop(0)]
        continue

    if len(strs) == 0:
        res_list.append(curr_anagrams_list)
            
    print(res_list)
    return res_list


def test():
    # L = [["bat"],["nat","tan"],["ate","eat","tea"]]
    # print('bat' in L[0])
    # print(['bat'] in L)
    # print(['nat'] in L)
    strs = ["",""]
    assert groupAnagrams(strs) == [["", ""]]

    strs = ["eat","tea","tan","ate","nat","bat"]
    assert groupAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    # groupAnagrams(strs)


if __name__ == '__main__':
    test()