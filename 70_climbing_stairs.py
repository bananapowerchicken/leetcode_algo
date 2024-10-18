


# https://leetcode.com/problems/climbing-stairs/
from math import factorial

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    num1 = n  # число единиц
    num2 = 0  # число двоек
    res = 1
    if n == 1:
        return res
    
    lngth = n  # длина массива из 1 и 2, меньше, чем n
    while lngth >= 1:
        num2 += 1
        num1 -= 2
        lngth -= 1
        if num1 < 0:
            break
        num_swaps = factorial(lngth) / factorial(num1) / factorial(num2)
        res += int(num_swaps) 

    return res

             

def test():
    n = 3
    assert climbStairs(n) == 3

    n = 4
    assert climbStairs(n) == 3

if __name__ == '__main__':
    test()