def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = [float('inf')] * (total + 1)
    num_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                num_coins[i] = min(num_coins[i], num_coins[i - coin] + 1)

    if num_coins[total] == float('inf'):
        return -1

    return num_coins[total]
