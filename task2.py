from typing import Callable

def generator_numbers(text: str):

    for word in text.split():               # Розділяємо текст на окремі слова
        try:
            number = float(word)            # Спробуємо конвертувати слово в дійсне число
            yield number                    # Якщо конвертація успішна, повертаємо число
        except ValueError:                  # Якщо конвертація невдала, пропускаємо
            continue
    
def sum_profit(text: str, func: Callable):
    total_profit = sum(func(text))          # Обчислюємо суму чисел, використовуючи генератор
    return total_profit
    
text = "Зарплата за перший місяць 30500.5 грн, за другий - 33700.75 грн, a за третій - 28200 грн."

summa_profits = sum_profit(text, generator_numbers)
print(f"Загальний прибуток за три місяці: {summa_profits} грн")



