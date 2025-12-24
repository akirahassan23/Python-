prices = [7, 1, 5, 3, 6, 4]
min_price = prices[0]  # the lowest price seen so far
max_profit = 2  # best profit found so far

for price in prices:
    # check if this price gives better profit
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit

    # update minimum price if current price is lower
    if price < min_price:
        min_price = price

print("Maximum Profit:", max_profit)
