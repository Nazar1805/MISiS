a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
operator = input('Введите один из знаков - "+", "-", "*", "/": ')
while operator not in '+-*/':
    print('Введен некорректный символ')
    operator = input('Введите один из знаков - "+", "-", "*", "/": ')
if operator == '+':
    print('Результат равен ', a+b)
elif operator == '-':
    print('Результат равен ', a-b)
elif operator == '*':
    print('Результат равен ', a*b)
else:
    while b == 0:
        print('На ноль делить нельзя!')
        b = int(input('Введите второе число заново: '))
    print('Результат равен ', a/b)