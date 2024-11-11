# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    p_min = 10001  # more than max possible in task
    max_profit = 0

    for p in prices:
        p_min = min(p, p_min)
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