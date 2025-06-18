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

    res = find_min_coins(target_sum, banknotes)
    print(res)