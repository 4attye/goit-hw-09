import timeit


def find_coins_greedy(amount, banknotes):
    
    banknotes = sorted(banknotes, reverse=True)  
    result = {}

    # Основний цикл для greedy алгоритму, перебираємо банкноти
    for bill in banknotes:
        count = amount // bill
        if count > 0:
            result[bill] = count
            amount -= bill * count

    return result


def find_min_coins(amount, banknotes):
    # Ініціалізуєм таблиці dp
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 

    # prev зберігатиме останню використану монету для побудови суми
    prev = [None] * (amount + 1)

    # Основний цикл для заповнення dp
    for bill in banknotes:
        for i in range(bill, amount + 1):
            if dp[i - bill] + 1 < dp[i]:
                dp[i] = dp[i - bill] + 1
                prev[i] = bill

    # Якщо сума не може бути досягнута, повертаємо порожній словник
    if dp[amount] == float('inf'):
        return {}

    # Відновлеєм результат
    result = {}
    current = amount
    while current > 0:
        bill = prev[current]
        if bill is None:
            break
        result[bill] = result.get(bill, 0) + 1
        current -= bill

    return result

if __name__ == "__main__":
   
    target_sum = 113 
    banknotes = [50, 25, 10, 5, 2, 1]

    res = find_coins_greedy(target_sum, banknotes)
    print(res)

    res = find_min_coins(target_sum, banknotes)
    print(res)

    # setup = f"from __main__ import find_coins_greedy, find_min_coins, target_sum, banknotes"

    # t_find_coins_greedy = timeit.timeit("find_coins_greedy(target_sum, banknotes.copy())"
    #                                     , setup=setup
    #                                     , number=1)
    
    # t_find_min_coins = timeit.timeit("find_min_coins(target_sum, banknotes.copy())"
    #                                  , setup=setup
    #                                  , number=1)

    # print(f"Time for greedy algorithm: {t_find_coins_greedy:.6f} seconds")
    # print(f"Time for dynamic programming algorithm: {t_find_min_coins:.6f} seconds")