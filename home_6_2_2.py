# Функція для переведення секунд у дні, години, хвилини та секунди
def convert_seconds(seconds):
    if seconds < 0 or seconds >= 8640000:
        print("Число повинно бути більше або дорівнює 0 і менше ніж 8640000.")
        return

    days = seconds // 86400  # 1 день = 86400 секунд
    hours = (seconds % 86400) // 3600  # 1 година = 3600 секунд
    minutes = (seconds % 3600) // 60  # 1 хвилина = 60 секунд
    remaining_seconds = seconds % 60  # решта секунд

    # Виведення результату
    print(f"{days} днів, {hours} годин, {minutes} хвилин, {remaining_seconds} секунд")

# Введення числа
seconds_input = int(input("Введіть число секунд (від 0 до 8639999): "))
convert_seconds(seconds_input)

