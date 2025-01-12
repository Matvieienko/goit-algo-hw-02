import queue
import time


# Створити чергу заявок
request_queue = queue.Queue()

# Лічильник для створення унікальних заявок
request_id = 1

# Функція для генерації нових заявок
def generate_request():
    global request_id
    request_queue.put(request_id)
    print(f"Generated: request nr {request_id}")
    request_id += 1
    time.sleep(1)  # Імітація часу на обробку заявки

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing: request nr {request}")
        time.sleep(1)  # Імітація часу на обробку заявки
    else:
        print("Queue is empty. No requests to process.")

# Головний цикл програми, вихід з програми Ctrl+C
try:
    while True:
        print("\n--- New Cycle ---")
        time.sleep(1)  # Імітація часу на обробку заявки
        generate_request()  # Створення нової заявки
        process_request()  # Обробка заявки
except KeyboardInterrupt:
    print("\nProgram stopped by user.")