# Функція для переведення секунд у дні, години, хвилини та секунди
import datetime

value_input = int(input("Введіть число секунд (від 0 до 8640000): "))

if value_input > 0 or value_input <= 8640000:

    time_delta = datetime.timedelta(seconds=value_input)

    # Обчислення днів, годин, хвилин та секунд
    days = time_delta.days
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Вибір правильної форми для слова "день"
    if days % 10 == 1:
        day_str = "день"
    elif 2 <= days <= 4:
        day_str = "дні"
    elif days > 4 or days == 0:
        day_str = "днів"

    print(f"{days} {day_str}, {hours:02}:{minutes:02}:{seconds:02}")

else:
    print("Число повинно бути більше або дорівнює 0 і менше ніж 8640000.")
