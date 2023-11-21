# https://leetcode.com/problems/sqrtx/description/
import math

def getSqrt(x):
    """
    :type x: int
    :rtype: int
    """
    base_sqr = 0 # ближайший квадрат числа
    res = -1
    
    while True:
        sqr = base_sqr * base_sqr
        if x < sqr:
            res = base_sqr - 1
        if x == sqr:
            res = base_sqr
        else:
            base_sqr += 1
        if res >= 0:
            break
        

    print(res)

    return res
             

def test():
    n = 0
    assert getSqrt(n) == 0

    n = 1
    assert getSqrt(n) == 1

    n = 2
    assert getSqrt(n) == 1

    n = 3
    assert getSqrt(n) == 1

    n = 4
    assert getSqrt(n) == 2

    n = 7
    assert getSqrt(n) == 2

    n = 9
    assert getSqrt(n) == 3

    n = 15
    assert getSqrt(n) == 3

    n = 99
    assert getSqrt(n) == 9

    n = 255
    assert getSqrt(n) == 15

if __name__ == '__main__':
    test()