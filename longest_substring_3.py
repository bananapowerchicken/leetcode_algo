# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    s_len = len(s)
    s_uniq = ''
    s_uniq_start = 0 # индекс начала уникальной строки во входной
    res_len = 0
    
    if s_len < 2:
        return s_len
    
    for i in range(s_len):
        # print(i)
        if s[i] in s_uniq:
            same_index = s_uniq.find(s[i])
            s_uniq = s_uniq[same_index + 1: i + 1] + s[i] # начать после вхождения повтора - сдвинуть старт
            s_uniq_start = s_uniq_start + same_index + 1
            # if res_len < len(s_uniq):
            #     res_len = len(s_uniq)
        else:
            s_uniq += s[i]
            # res_len = len(s_uniq)

        if res_len < len(s_uniq):
            res_len = len(s_uniq)


    return res_len
             

def test():

    s = 'nfpdmpi'
    assert lengthOfLongestSubstring(s) == 5
    
    s = 'dvdf'
    assert lengthOfLongestSubstring(s) == 3

    s = 'au'
    assert lengthOfLongestSubstring(s) == 2

    s = 'abcabcbb'
    assert lengthOfLongestSubstring(s) == 3

    s = 'bbbbb'
    assert lengthOfLongestSubstring(s) == 1

    s = 'pwwkew'
    assert lengthOfLongestSubstring(s) == 3

if __name__ == '__main__':
    test()