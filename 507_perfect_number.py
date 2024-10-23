# https://leetcode.com/problems/perfect-number
# easy

def checkPerfectNumber(num) -> bool:
    """
    :type num: int
    :rtype: bool
    """
    if num <= 1 or num == 6:
        return True
    if num < 10:
        return False
    div_sum = 1
    for d in range(2, num // 2 + 1):
        if num % d == 0:
            div_sum += d
    
    return div_sum == num





def test():
    num = 99999991
    assert checkPerfectNumber(num) == False


if __name__ == '__main__':
    test()


# find all positive divisors
# check sum
# 1 = 1 t
# 2 = 1 f
# 3 = 1 f
# 4 = 1 + 2 f
# 5 = 1 f
# 6 = 1 + 2 + 3 t
# 7 = 1 f
# 8 = 1 + 2 + 4 f
# 9 = 1 + 3 f
