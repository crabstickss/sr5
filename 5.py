try:
    time_hours_1 = int(input("Введите часы первого промежутка: "))
    time_minutes_1 = int(input("Введите минуты первого промежутка: "))
    time_hours_2 = int(input("Введите часы второго промежутка: "))
    time_minutes_2 = int(input("Введите минуты второго промежутка: "))
except:
    print("Ошибка")
else:
    time_in_minutes_1 = time_hours_1*60 + time_minutes_1
    time_in_minutes_2 = time_hours_2*60 + time_minutes_2

    if time_in_minutes_1 > time_in_minutes_2:
        print(time_in_minutes_1 - time_in_minutes_2)
    else:
        print("Временной промежуток в минутах =" + str(time_in_minutes_2 - time_in_minutes_1))
