# https://leetcode.com/problems/find-the-town-judge
# easy

def findJudge(n, trust) -> bool:
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    nums = [x for x in range(1, n+1)]
    trusting_list = [trust[x][0] for x in range(len(trust))]
    trusted_list = [trust[x][1] for x in range(len(trust))]

    if nums == sorted(set(trusting_list)):
        return -1

    # find who trusts nobody
    for i in nums:
        print('curr num ', i)
        if i not in trusting_list:
            # check if judge exists
            if trusted_list.count(i) == n-1:
                return i
    
    return -1






def test():
    n = 2
    trust = [[1,2]]
    assert findJudge(n, trust) == 2

    n = 3
    trust = [[1,3],[2,3]]
    assert findJudge(n, trust) == 3

    n = 3
    trust = [[2,3],[1,3],[3,1]]
    assert findJudge(n, trust) == -1


if __name__ == '__main__':
    test()


# everybody trusts the judge, so if x is combinated with each num - it is judge
# otherwise - it doesn't

# or i can find the n that trusts nobody and then check it

# if trusting list have all the nums - no judge
