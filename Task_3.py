import sys
sys.stdout.reconfigure(encoding='utf-8')


def check_brackets(expression):
    # Стек для зберігання відкритих дужок
    stack = []
    # Відповідність відкритих і закритих дужок
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        # Якщо символ - це відкрита дужка, додаємо в стек
        if char in "([{":
            stack.append(char)
        # Якщо символ - це закрита дужка
        elif char in ")]}":
            # Перевіряємо, чи стек не порожній і чи відповідає остання відкрита дужка
            if stack and stack[-1] == bracket_pairs[char]:
                stack.pop()  # Видаляємо останню відкриту дужку зі стеку
            else:
                return "Несиметрично"

    # Якщо стек порожній, дужки симетричні
    return "Симетрично" if not stack else "Несиметрично"

# Приклад використання
expressions = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
        ]

for expr in expressions:
    result = check_brackets(expr)
    print(f"'{expr}': {result}")