num = int(input('Введите количество секунд:'))
day, hour, minute = 0, 0, 0
if num < 60:
    print(day, 'дней', hour, 'часов', minute, 'минут', num, 'секунд')
elif 3600 > num >= 60:
    minute = num // 60
    num = num % 60
    print(day, 'дней', hour, 'часов', minute, 'минут', num, 'секунд')
elif 86400 > num >= 3600:
    hour = num // 3600
    minute = (num % 3600) // 60
    num = (num % 3600) % 60
    print(day, 'дней', hour, 'часов', minute, 'минут', num, 'секунд')
else:
    day = num // 86400
    hour = (num % 86400) // 3600
    minute = ((num % 86400) % 3600) // 60
    num = ((num % 86400) % 3600) % 60
    print(day, 'дней', hour, 'часов', minute, 'минут', num, 'секунд') 