# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# easy
# strings

# complexity 
# time: O(n^2) - once go through list 
# space O(n) - only vars

# 2 pointers - good

# -------------1
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     longest_substring = ''    
#     i1 = 0
#     i2 = 0
#     curr_substring = '' # adds O(n) space

#     while i2 < len(s):
#         if s[i2] not in curr_substring:
#             curr_substring += s[i2]
#             i2 += 1
#         else:
#             i1 = i1 + curr_substring.find(s[i2]) + 1 # find adds O(n) -> O(n^2) time
#             i2 += 1
#             curr_substring = s[i1:i2]
        
#         if len(curr_substring) > len(longest_substring):
#             longest_substring = curr_substring
    
#     return len(longest_substring)


# -------------2
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     left = 0    
#     curr_str = ''
#     max_len = 0

#     for right in range(len(s)):
#         if s[right] in curr_str:
#             left += curr_str.find(s[right]) + 1
#             # max_len = max(max_len, len(curr_str))
#             curr_str = s[left:right+1]
#         else:
#             curr_str += s[right]
#         max_len = max(max_len, len(curr_str))
    
#     return max_len


# -------------3 - without find() and slicing - n complexity
# set + 2 pointers
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    seen = set()
    left = 0
    max_len = 0

    for right in (range(len(s))):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, len(seen)) # right - left + 1
    return max_len






             

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