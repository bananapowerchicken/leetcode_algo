# https://leetcode.com/problems/roman-to-integer/
    # 'IV' - 4
    # 'IX' - 9
    # 'XL' - 40
    # 'XC' - 90
    # 'CD' - 400
    # 'CM' - 900

def romanToInt(s):
    alphabet = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }
    res = 0
    len_s = len(s)
    i = 0

    while i < len_s:
        
        if i != len_s - 1:
            pair = s[i] + s[i+1]            
            if pair in alphabet:
                res += alphabet[s[i] + s[i+1]]
                i += 2
            else:
                res += alphabet[s[i]]
                i += 1
        else:
            res += alphabet[s[i]]
            i += 1
        
    print(res)
    return res


def test():
    s = "III"
    assert romanToInt(s) == 3

    s = "LVIII"
    assert romanToInt(s) == 58

    s = "MCMXCIV"
    assert romanToInt(s) == 1994

    s = "MCDLXXVI"
    assert romanToInt(s) == 1476


if __name__ == '__main__':
    test()