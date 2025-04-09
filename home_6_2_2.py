
import datetime

value_input = int(input("Введіть число секунд (від 0 до 8640000): "))

if 0 < value_input <= 8640000:

    time_delta = datetime.timedelta(seconds=value_input)

    days = time_delta.days
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days % 10 == 1 and days != 11:
        day_str = "день"
    elif 2 <= days <= 4 or days % 10 == 2 and days !=12 or days % 10 == 3 and days !=13 or days % 10 == 4 and days !=14 :
        day_str = "дні"
    elif 4 < days <= 20 or days == 0 or days == 11 or days % 10 == 0 or days % 10 == 9 or days % 10 == 8 or days % 10 == 7 or days % 10 == 6 or days % 10 == 5:
        day_str = "днів"

    print(f"{days} {day_str}, {hours:02}:{minutes:02}:{seconds:02}")

else:
    print("Число повинно бути більше або дорівнює 0 і менше ніж 8640000.")
