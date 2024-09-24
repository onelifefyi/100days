# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Approach:
# Take all possible values, find the max profit
# Time O(n^2) | Space O(1)

# Approach:
# Keep track of min_price
# Keep track of max (say result) which contains max(result, num - min_price)
# At the end return result
# Time O(n) | Space O(1)
def maxProfit(prices):
    min_price = prices[0]
    result = 0
    for price in prices:
        min_price = min(price, min_price)
        result = max(result, price - min_price)
    return result

# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(maxProfit(prices))