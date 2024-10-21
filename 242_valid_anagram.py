# https://leetcode.com/problems/valid-anagram/
# easy

def isAnagram(s, t) -> bool:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_sorted = ''.join(sorted(s))
    t_sorted = ''.join(sorted(t))
    return s_sorted == t_sorted




def test():
    s = 'anagram'
    t = 'nagaram'
    assert isAnagram(s, t) == True

    s = 'rat'
    t = 'car'
    assert isAnagram(s, t) == False


if __name__ == '__main__':
    test()


# just calc matching letters and their amounts
# so comparison of two dicts