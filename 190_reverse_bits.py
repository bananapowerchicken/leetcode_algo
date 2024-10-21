# https://leetcode.com/problems/reverse-bits/
# easy

def reverseBits(n: int) -> int:
    # @param n, an integer
    # @return an integer
    # have a standart dec n in input
    # bin_num = '{:032b}'.format(n)
    # res = int(bin_num[::-1], 2)
    # return res

    return int('{:032b}'.format(n)[::-1], 2)


def test():
    n = 43261596
    assert reverseBits(n) == 964176192


if __name__ == '__main__':
    test()