def caching_fibonacci():
    cache = {} # Словник для зберігання результатів обчислення чисел Фібоначчі
    
    def fibonacci(n): # Створення внутрішньої функції fibonacci
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: # Перевірка наявності n у cache
            return cache[n] # Повернення результату зі словника
        else: # Якщо значення відсутнє у кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Запис в словник результату виконання
        return cache[n]

    return fibonacci
# Створення замикання
fib = caching_fibonacci()
print(fib(10))
print(fib(15))