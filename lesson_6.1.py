seconds_amount = int(input("enter amount of seconds(0 ≤ n < 8640000): "))

days , remainder = divmod(seconds_amount, 86400)
hours , remainder= divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)


time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


if days % 10 == 1 and days % 100 != 11:
    day_word = "day"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "days"
else:
    day_word = "days"


print(f"{days} {day_word}, {time_str}")

