# https://leetcode.com/problems/longest-palindromic-substring

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    len_s = len(s)
    longest_palindrom = getPalindrom(s, 0, 0)
    
    for i in range(len_s - 1):

        if i+1 < len_s and s[i] == s[i+1]:
            res1 = getPalindrom(s, i, i+1)
            res2 = getPalindrom(s, i, i)
            res = res1 if  len(res1) > len(res2) else res2
        else:
            res = getPalindrom(s, i, i)
        if len(res) > len(longest_palindrom):
            longest_palindrom = res
    
    return longest_palindrom


def getPalindrom(s, i, j):
    left = i - 1
    right = j + 1
    res = s[i:j+1]
    while left > -1 and right < len(s):
        if s[left] == s[right]:
            res = s[left: right + 1]
            left -= 1
            right += 1
        else:
            break
    
    return res

             

def test():
    s = 'SQQSYYSQQS'
    assert longestPalindrome(s) == 'SQQSYYSQQS'
    
    s = 'aaaaa'
    assert longestPalindrome(s) == 'aaaaa'

    s = 'aaaa'
    assert longestPalindrome(s) == 'aaaa'
    
    s = 'cbbc'
    assert longestPalindrome(s) == 'cbbc'



    


if __name__ == '__main__':
    test()


# i need the longest palindrom string
# a - center
# aa - center

