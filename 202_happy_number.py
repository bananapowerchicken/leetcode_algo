# https://leetcode.com/problems/happy-number/
# easy

def isHappy(n) -> bool:
    """
    :type n: int
    :rtype: bool
    """
    if n == 1 or n == 7:
        return True
    if  1 < n < 10:
        return False

    res = 0

    curr_main_part = n // 10
    curr_dig_rest = n % 10

    while curr_main_part > 0:
        res += curr_dig_rest**2
        curr_dig_rest = curr_main_part % 10
        curr_main_part = curr_main_part // 10
    res += curr_dig_rest**2
    print(res)

    return isHappy(res)
        


    


def test():
    # n = 19
    # assert isHappy(n) == True

    # n = 2
    # assert isHappy(n) == False

    isHappy(9)

if __name__ == '__main__':
    test()

# can bee very long number
# take num
# put to digits
# sum all digits square
# repeat with result until the result is not 1