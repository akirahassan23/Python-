def coin_change(coins, amount):
    # Step 1: Create DP array
    dp = [float("inf")] * (amount + 1)

    # Step 2: Base case
    dp[0] = 0

    # Step 3: Fill DP array
    for coin in coins:
        for amt in range(coin, amount + 1):
            dp[amt] = min(dp[amt], 1 + dp[amt - coin])

    # Step 4: Return answer
    return dp[amount] if dp[amount] != float("inf") else -1