# https://leetcode.com/problems/longest-palindromic-substring

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    res_palindrom = s[0]
    curr_palindrom = ''

    if len(s) == 1:
        return res_palindrom
    


    # for i in range(len(s) - 1):
        # print(f'curr ind: {i}')

        # if s[i] == s[i+1]:
        #     if i+2 < len(s) and s[i] == s[i+2]:
        #         curr_palindrom = s[i:i+3]
        #         left = i - 1
        #         right = i + 3 
        #     else:
        #         curr_palindrom =  s[i:i+2]
        #         left = i - 1
        #         right = i + 2        
        # else:
        #     curr_palindrom = s[i]
        #     left = i - 1
        #     right = i + 1
        
        
        # while left > -1 and right < len(s):
        #     if s[left] == s[right]:
        #         curr_palindrom = s[left : right + 1]
        #     else:
        #         break
        #     left -= 1
        #     right += 1

    for i in range(1, len(s)):
        left = i - 1
        right = i + 1

        if s[i] == s[right]:
            right += 1
        
        while left > -1 and right < len(s):
            if s[left] == s[right]:
                curr_palindrom = s[left : right + 1]
            else:
                break
            left -= 1
            right += 1




        
        print(curr_palindrom)

        if len(curr_palindrom) > len(res_palindrom):
            res_palindrom = curr_palindrom
    
    return res_palindrom

             

def test():
    # s = 'babad'
    # assert longestPalindrome(s) == 'bab'
    
    # s = 'cbbd'
    # assert longestPalindrome(s) == 'bb'

    # s = 'abaab'
    # assert longestPalindrome(s) == 'baab'

    # s = 'baab'
    # assert longestPalindrome(s) == 'baab'

    s = 'aaaa'
    assert longestPalindrome(s) == 'aaaa'

    


if __name__ == '__main__':
    test()


# i need the longest palindrom string

