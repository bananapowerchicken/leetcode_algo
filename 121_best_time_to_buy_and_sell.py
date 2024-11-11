# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    i_start = 0
    res = 0

    while i_start < len(prices) - 1:
        tmp_arr = [prices[i] - prices[i_start] for i in range(i_start + 1, len(prices))] # eats much time
        if max(tmp_arr) > res:
            res = max(tmp_arr)
        i_start += 1
    
    return res

        
        
        

def test():
    prices = [2,4,1]
    assert maxProfit(prices) == 2

    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0


if __name__ == '__main__':
    test()