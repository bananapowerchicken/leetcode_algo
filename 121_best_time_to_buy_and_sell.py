# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    while len(prices) >= 2:
        min_p = min(prices)
        min_i = prices.index(min_p)

        if min_i + 1 < len(prices):
            max_p = max(prices[min_i + 1::])
        else:
            prices.pop(min_i)
            continue

        if max_p > min_p:
            return max_p - min_p
        else:
            return 0
        
        
        

def test():
    prices = [2,4,1]
    assert maxProfit(prices) == 5

    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0


if __name__ == '__main__':
    test()