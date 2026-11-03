import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Аналізує текст, знаходить усі дійсні числа, що відокремлені пробілами,
    і повертає їх через конструкцію yield як генератор.
    """
    
    pattern = r'(?:\s)\d+\.\d+(?=\s)' # патерн дійсного числа з пробілом на початку і в кінці
    # (?:\s) —  пробіл на початку рядка.
    # \d+\.\d+ — дійсне число.
    # (?=\s) - пробіл в кінці рядка.

    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обробляє дані від генератора та підсумовує всі знайдені числа,
    обчислюючи загальний прибуток.
    """
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")