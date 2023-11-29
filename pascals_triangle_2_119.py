# https://leetcode.com/problems/pascals-triangle-ii/

def count_pairs(row):
    res = [1]
    for i in range(len(row) - 1):
        res.append(row[i] + row[i+1])
    res = res + [1]
    return res

def getRow(rowIndex):
    curr_row = [1]
    if rowIndex == 0:
        return curr_row
    
    curr_row =  [1, 1]
    if rowIndex == 1:
        return curr_row

    for i in range(1, rowIndex):
        curr_row = count_pairs(curr_row)        
    
    return curr_row



def test():
    n = 0
    assert getRow(n) == [1]

    n = 1
    assert getRow(n) == [1, 1]

    n = 2
    assert getRow(n) == [1, 2, 1]

    n = 3
    assert getRow(n) == [1, 3, 3, 1]

    n = 4
    assert getRow(n) == [1, 4, 6, 4, 1]


if __name__ == '__main__':
    test()