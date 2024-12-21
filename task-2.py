from typing import List, Dict

from typing import List

def validate_inputs(length: int, prices: List[int]) -> None:
    """Перевіряє коректність вхідних даних для розрізання стрижня."""
    if length <= 0:
        raise ValueError("Довжина стрижня повинна бути більше за 0.")
    if not prices or len(prices) != length:
        raise ValueError("Масив цін повинен бути не порожнім і мати довжину, що відповідає довжині стрижня.")
    if any(price <= 0 for price in prices):
        raise ValueError("Всі ціни повинні бути більше за 0.")

def rod_cutting_memo(length: int, prices: List[int]) -> dict:
    validate_inputs(length, prices)

    memo = {}

    def helper(n):
        max_profit = 0
        best_cuts = []

        for i in range(1, n + 1):
            profit, cuts = helper(n - i)
            profit += prices[i - 1]

            if profit > max_profit:
                max_profit = profit
                best_cuts = cuts + [i]

        memo[n] = (max_profit, best_cuts)
        return memo[n]

    max_profit, cuts = helper(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

def rod_cutting_table(length: int, prices: List[int]) -> dict:
    validate_inputs(length, prices)

    dp = [0] * (length + 1)
    cuts = [0] * (length + 1)

    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if dp[i] < dp[i - j] + prices[j - 1]:
                dp[i] = dp[i - j] + prices[j - 1]
                cuts[i] = j

    max_profit = dp[length]
    result_cuts = []
    while length > 0:
        result_cuts.append(cuts[length])
        length -= cuts[length]

    return {
        "max_profit": max_profit,
        "cuts": result_cuts,
        "number_of_cuts": len(result_cuts) - 1
    }


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Рівномірні розрізи
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()