# https://leetcode.com/problems/license-key-formatting
# complexity: 

def format_license_key(s, k) -> str:
    new_s = s.replace("-", "").upper() # delete - and make upper case
    new_len = len(new_s)
    R = new_len % k
    Z = new_len // k

    if new_len <= k:
        return new_s
    
    res_s = ""

    if R:
        res_s += new_s[0:R]
        res_s += "-"
    
    for i in range(Z):
        curr_i = R + k*i
        res_s += new_s[curr_i:curr_i + k]
        res_s += "-"
    
    return res_s[:-1]
    
     

def test():
    # s = "5F3Z-2e-9-w"
    # k = 4
    # target = "5F3Z-2E9W"
    # assert format_license_key(s, k) == target

    # s = "5F3Z-2e-9-w"
    # k = 8
    # target = "5F3Z2E9W"
    # assert format_license_key(s, k) == target

    # s = "5F3Z-2e-9-w"
    # k = 9
    # target = "5F3Z2E9W"
    # assert format_license_key(s, k) == target

    s = "2-5g-3-J"
    k = 2
    target = "2-5G-3J"
    assert format_license_key(s, k) == target

if __name__ == '__main__':
    test()