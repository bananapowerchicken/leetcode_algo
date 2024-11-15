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

    while len(strs) > 0:
        curr_anagrams_list = [strs.pop(0)]
        for s in strs:
            if isAnagram(s, curr_anagrams_list[0]):
                curr_anagrams_list.append(s)
        
        for el in curr_anagrams_list:
            if el in strs:
                strs.remove(el)
        res_list.append(curr_anagrams_list)

    return res_list
              



    


def test():
    strs = ["",""]
    assert groupAnagrams(strs) == [["", ""]]

    strs = ["eat","tea","tan","ate","nat","bat"]
    assert groupAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]]


if __name__ == '__main__':
    test()