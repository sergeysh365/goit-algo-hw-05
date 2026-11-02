import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Аналізує текст, розділяючи його по пробілах, та ідентифікує
    дійсні числа за допомогою re.match і yield.
    """
    # Регулярний вираз для перевірки, чи є слово цілим або дійсним числом.
    # ^\d+(?:\.\d+)?$ означає, що весь рядок від початку (^) до кінця ($) має бути числом.
    pattern = r'^\d+(?:\.\d+)?$'

    # Розбиваємо текст на окремі елементи по пробілах
    for word in text.split():
        if re.match(pattern, word):
            yield float(word) # повернення значення з генератора

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальний прибуток, використовуючи функцію-генератор.
    """
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")