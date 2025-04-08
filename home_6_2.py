value_input = int(input("Введіть число секунд (від 0 до 8640000): "))

if value_input > 0 or value_input <= 8640000:
    days, remainder = divmod(value_input, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days % 10 == 1:
        day_str = "день"
    elif 2 <= days <= 4:
        day_str = "дні"
    elif days > 4 or days == 0:
        day_str = "днів"

    # Формуємо рядок з годинами, хвилинами і секундами
    hour_str = f"{str(hours).zfill(2)}"
    minute_str = f"{str(minutes).zfill(2)}"
    second_str = f"{str(seconds).zfill(2)}"

    # Формуємо фінальний рядок
    print(f"{days} {day_str}, {hour_str}:{minute_str}:{second_str}")

else:
    print("Число повинно бути більше або дорівнює 0 і менше ніж 8640000.")