from pathlib import Path
import sys

def parse_log_line(line: str) -> dict: # функція для парсингу одного рядка логу в словник
    line = line.strip() # прибираємо зайві пробіли та символи переносу \n
    if not line:
        return {} # Якщо рядок порожній, повертаємо порожній словник
    try:
        # Розділення рядка за пробілами
        parts = line.split(' ')

        # Перевірка, чи достатньо елементів у рядку логу
        if len(parts) < 4:
            raise ValueError("Недостатньо даних у рядку")

        # Створення словника
        log_dict = {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": " ".join(parts[3:])
        }
        return log_dict

    except (ValueError, IndexError):
        print(f"Попередження: Некоректний формат даних у рядку: '{line}'")
        return {}


def load_logs(file_path: str) -> list: # функція для завантаження логів з файлу
    log_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file: # Зчитування з файлу рядок за рядком
                parsed_line = parse_log_line(line)
                if parsed_line:
                    log_list.append(parsed_line)
        return log_list

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Сталася непередбачена помилка при роботі з файлом: {e}")

    return []


def filter_logs_by_level(logs: list, level: str) -> list: # функція для фільтрації логів за рівнем
    filtered_logs = list(filter(lambda x: x.get('level').upper() == level.upper(), logs))
    return filtered_logs


def count_logs_by_level(logs: list) -> dict: # функція для підрахунку записів за рівнем логування
    counts = {}
    for log in logs:
        level = log.get('level')
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict): # функція яка форматує та виводить результати
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 18 + "|" + "-" * 11)
    for level, count in counts.items():
        print(f"{level:<17} | {count:<10}")


# Головний блок запуску через командний рядок
if __name__ == "__main__":
    # Перевірка наявності обов'язкового аргументу (шляху до файлу)
    if len(sys.argv) < 2:
        print("Помилка: Ви не вказали шлях до файлу логів!")
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    # Отримання шляху до файлу з першого аргументу
    file_path = sys.argv[1]

    # Завантаження всіх логів у список словників
    logs = load_logs(file_path)

    if logs:
        # Рахуємо кількість логів за рівнями та виводимо таблицю
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        # Перевірка, чи передано необов'язковий другий аргумент (рівень фільтрації)
        if len(sys.argv) > 2:
            search_level = sys.argv[2]
            filtered = filter_logs_by_level(logs, search_level)

            print("\n" + "="*40 + "\n")
            print(f"Деталі логів для рівня '{search_level.upper()}':")

            if filtered:
                for log in filtered:
                    print(f"{log['date']} {log['time']} - {log['message']}")
            else:
                print(f"Записів для рівня '{search_level.upper()}' не знайдено.")