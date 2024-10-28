# https://leetcode.com/problems/power-of-two
# easy

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """

    if n == 1:
        return True
    
    if n % 2 != 0 or n == 0:
        return False
    else:
        return isPowerOfTwo(n//2)
    



def test():
    n = 24
    assert isPowerOfTwo(n) == False

    n = 3
    assert isPowerOfTwo(n) == False

    n = 16
    assert isPowerOfTwo(n) == True



if __name__ == '__main__':
    test()