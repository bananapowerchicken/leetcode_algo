# https://leetcode.com/problems/zigzag-conversion/
# complexity: ?


def convert(s, numRows):

    if numRows == 1 or len(s) == 1:
        return s

    s_list = []
    for i in range(numRows):
        s_list.append('') # how exactly append works?
    diff_ind = 1  # marker to define current substring to append to
    s_index = -1  # current index of s_list to fill with current symb

    for i in range(len(s)):
        s_index += diff_ind
        s_list[s_index] += s[i]

        if s_index == numRows - 1:
            diff_ind = -1
        
        if s_index == 0:
            diff_ind = 1
    
    res = ''
    for i in range(numRows):
        res += s_list[i]
    
    print(res)
    return res

def test():
    s = 'PAYPALISHIRING'
    numRows = 1
    convert(s, numRows)
    assert convert(s, numRows) == 'PAYPALISHIRING'

    s = 'P'
    numRows = 4
    convert(s, numRows)
    assert convert(s, numRows) == 'P'

    s = 'PAYPALISHIRING'
    numRows = 3
    convert(s, numRows)
    assert convert(s, numRows) == 'PAHNAPLSIIGYIR'

    s = 'PAYPALISHIRING'
    numRows = 4
    convert(s, numRows)
    assert convert(s, numRows) == 'PINALSIGYAHRPI'


if __name__ == '__main__':
    test()