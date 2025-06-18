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

if __name__ == "__main__":
   
    target_sum = 113 
    banknotes = [50, 25, 10, 5, 2, 1]

    res = find_coins_greedy(target_sum, banknotes)
    print(res)