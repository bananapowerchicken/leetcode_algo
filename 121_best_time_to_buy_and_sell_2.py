# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy
# arrays


# complexity 
# time: O(n) - once go through list 
# space O(1) - only vars

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    p_min = 10000000 # absurdly big number
    max_profit = -1000000
    for p in prices:
        p_min = min(p_min, p)
        max_profit = max(max_profit, p - p_min)

    return max_profit 
        

def test():
    prices = [2,4,1]
    assert maxProfit(prices) == 2

    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0


if __name__ == '__main__':
    test()