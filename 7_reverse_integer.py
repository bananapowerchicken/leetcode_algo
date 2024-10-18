# https://leetcode.com/problems/reverse-integer/

def reverse(x):
    max_limit = pow(2, 31) - 1
    min_limit = -1 * pow(2, 31)

    res = 0
    minus = False
    int_part = 1
    rest_part = 0

    if x < 0:
        x = x * -1
        minus = True

    while int_part > 0:
        rest_part = x % 10
        x = int_part = x // 10        
        res = res*10 + rest_part  

    if minus:
        res = res * -1

    if min_limit <= res <= max_limit:
        return res
    else:
        return 0
    # return res


def test():
    # n = 123
    # assert reverse(n) == 321

    n = -123
    assert reverse(n) == -321


if __name__ == '__main__':
    test()
