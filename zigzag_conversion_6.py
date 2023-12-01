# https://leetcode.com/problems/zigzag-conversion/
# complexity: ?


def convert(s, numRows):
    s1 = s2 = s3 = s4 = ''
    s_list = [s1, s2, s3, s4]
    s_index = 0  # current index of s_list to fill with current symb

    for i in range(len(s)):
        s_list[s_index] += s[i]
        if s_index < numRows:
            s_index += 1
        else:
            s_index -= 1




def test():
    s = 'PAYPALISHIRING'
    numRows = 3
    convert(s, numRows)
    # assert convert(s, numRows) == ''


if __name__ == '__main__':
    test()