# https://leetcode.com/problems/rectangle-overlap
# easy

def isRectangleOverlap(rec1, rec2):
    """
    :type rec1: List[int]
    :type rec2: List[int]
    :rtype: bool
    """   
    x_intersect = rec2[0] < rec1[2] < rec2[2] or rec1[0] < rec2[2] < rec1[2]
    y_intersect = rec2[1] < rec1[3] < rec2[3] or rec1[1] < rec2[3] < rec1[3]
    print(x_intersect and y_intersect)
    return x_intersect and y_intersect
        

def test():
    # x1, y1, x2, y2
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    assert isRectangleOverlap(rec1, rec2) == True

    rec1 = [0,0,1,1]
    rec2 = [1,0,2,1]
    assert isRectangleOverlap(rec1, rec2) == False


if __name__ == '__main__':
    test()