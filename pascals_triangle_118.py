# https://leetcode.com/problems/pascals-triangle/

def count_pairs(l: list):
    res = []
    for i in range(0, len(l) - 1):
        res.append(l[i] + l[i+1])
        i += 1
    
    return res

def generate(numRows):
    res = [[1]]

    if numRows == 1:
        return res
    
    res.append([1, 1])

    if numRows == 2:        
        return res
    
    i = 2
    while i < numRows:
        sublist = [1]
        middle = count_pairs(res[i-1])
        sublist += middle
        sublist.append(1)
        res.append(sublist)
        i += 1
    
    return res

             

def test():
    n = 1
    assert generate(n) == [[1]]

    n = 2
    assert generate(n) == [[1], [1, 1]]

    n = 3
    assert generate(n) == [[1], [1, 1], [1, 2, 1]]

    n = 4
    assert generate(n) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

    n = 5
    assert generate(n) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

if __name__ == '__main__':
    test()