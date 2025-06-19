"""
Problem: Best Time to Buy and Sell Stock (Single Transaction)

You are given an array A, where A[i] is the price of a stock on day i.
You can buy and sell the stock once (buy before sell).
Return the maximum profit you can achieve. If no profit, return 0.

Example:
Input  : A = [9, 8, 7, 10, 11]
Output : 4  (Buy at 7, sell at 11)
"""

def max_profit(A):
    if not A:
        return 0

    min_price = float('inf')   # Lowest price so far (best buying point)
    max_profit = 0             # Highest profit so far

    for price in A:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit

# Example usage
if __name__ == "__main__":
    A1 = [1, 2]
    A2 = [1, 4, 5, 2, 4]
    A3 = [9, 8, 7, 10, 11]

    print("Max profit A1:", max_profit(A1))  # Output: 1
    print("Max profit A2:", max_profit(A2))  # Output: 4
    print("Max profit A3:", max_profit(A3))  # Output: 4
