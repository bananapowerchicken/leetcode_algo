# find the most frequent char in string

# time complexity O(n) 
# space complexity O(n) 

def lengthOfLongestSubstring(s: str) -> str:
    chars = {}
    for ch in s:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    
    max_frequency = max(chars, key=chars.get) # any function can be here
    print(type(max_frequency))
    return max_frequency

# 2
# from collections import Counter

# def freqSymb(s: str) -> str:
#     counts = Counter(s)
#     return max(counts, key=counts.get)

             

def test():

    # s = 'nfpdmpi'
    # assert lengthOfLongestSubstring(s) == 5
    
    # s = 'dvdf'
    # assert lengthOfLongestSubstring(s) == 3

    # s = 'au'
    # assert lengthOfLongestSubstring(s) == 2

    s = 'abcabcbb'
    assert lengthOfLongestSubstring(s) == 'b'

    # s = 'bbbbb'
    # assert lengthOfLongestSubstring(s) == 1

    # s = 'pwwkew'
    # assert lengthOfLongestSubstring(s) == 3

if __name__ == '__main__':
    test()