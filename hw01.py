import timeit


# Жадібний алгоритм
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount -= coin * result[coin]

    return result


# Алгоритм динамічного програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 1]
    min_coins = [float("inf")] * (amount + 1)
    coin_used = [0] * (amount + 1)

    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


print(find_coins_greedy(113))
print(find_min_coins(113))

# Вимірювання часу для find_coins_greedy
time_greedy = timeit.timeit("find_coins_greedy(11131)", globals=globals(), number=1000)
print(f"Жадібний алгоритм виконався за: {time_greedy:.6f} секунд")

# Вимірювання часу для find_min_coins
time_dynamic = timeit.timeit("find_min_coins(11131)", globals=globals(), number=1000)
print(f"Алгоритм динамічного програмування виконався за: {time_dynamic:.6f} секунд")
