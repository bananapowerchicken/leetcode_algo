# https://leetcode.com/problems/ugly-number/
# easy

def isUgly(n):
    """
    :type n: int
    :rtype: bool
    prime factors 2, 3 or 5
    """
    PRIME_FACTORS = [2, 3, 5]
    res = n 

    while abs(res) != 1:
        for p in PRIME_FACTORS:
            if res % p == 0:
                res /= p
                
            else:
                continue
        if abs(res) != 1:
            return False
        
    
    return True



def test():

    n = 8
    assert isUgly(n) == True

    n = 0
    assert isUgly(n) == False

    n = 1
    assert isUgly(n) == True

    n = 5
    assert isUgly(n) == True

    n = 6
    assert isUgly(n) == True

    n = 14
    assert isUgly(n) == False

if __name__ == '__main__':
    test()