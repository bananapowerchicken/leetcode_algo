# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# easy
# strings

# complexity 
# time: O(n) - once go through list 
# space O(1) - only vars

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest_substring = ''    
    i1 = 0
    i2 = 0
    curr_substring = ''

    while i2 < len(s):
        if s[i2] not in curr_substring:
            curr_substring += s[i2]
            i2 += 1
        else:
            i1 = i1 + curr_substring.find(s[i2]) + 1
            i2 += 1
            curr_substring = s[i1:i2]
        
        if len(curr_substring) > len(longest_substring):
            longest_substring = curr_substring
    
    return len(longest_substring)





             

def test():

    # s = 'nfpdmpi'
    # assert lengthOfLongestSubstring(s) == 5
    
    # s = 'dvdf'
    # assert lengthOfLongestSubstring(s) == 3

    # s = 'au'
    # assert lengthOfLongestSubstring(s) == 2

    s = 'abcabcbb'
    assert lengthOfLongestSubstring(s) == 3

    s = 'bbbbb'
    assert lengthOfLongestSubstring(s) == 1

    s = 'pwwkew'
    assert lengthOfLongestSubstring(s) == 3

if __name__ == '__main__':
    test()