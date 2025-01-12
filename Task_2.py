from collections import deque

import sys
sys.stdout.reconfigure(encoding='utf-8')


def is_palindrome(text):
    # Приведення рядка до нижнього регістру і видалення пробілів
    clean_string = ''.join(char.lower() for char in text if char.isalnum())

    # Створення двосторонньої черги
    char_deque = deque(clean_string)

    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        left = char_deque.popleft()  # Видаляємо символ з лівого кінця
        right = char_deque.pop()    # Видаляємо символ з правого кінця
        if left != right:
            return "Ні, рядок не є паліндромом."

    return "Так, рядок є паліндромом."


# Приклад використання
print("Приклади використання:")
test_strings = [
            "123454321",
            "1234564321",
            "А роза упала на лапу Азора",
            "Не кабан, а банка",
            "Я несу гусеня"
            ]

for test in test_strings:
    print(f"'{test}': ", is_palindrome(test))
    
text = input("Введить текст для перевірки: \n")
print(f"'{text}': ", is_palindrome(text))
