# Создаем класс для расчетов

class class_calc:
    # Создаем запрос который получает из программы переменные
    def __init__(self, x, z, y):

            # Прописываем услловия выполнения операций и ошибок
            if z == '+':
                rezult = float(x) + float(y)
            elif z == '-':
                rezult = float(x) - float(y)
            elif z == '*':
                rezult = float(x) * float(y)
            else:
                if float(y) != 0 and z == '/':
                    rezult = float(x) / float(y)
                else:
                    if float(y) == 0:
                        rezult = 'Деление на ноль невозможно!'
                    else:
                        rezult = 'Введен неверный знак операции! Попробуйте снова!'
            print('Результат =', rezult)

# Тело программы
i = 1
while i == 1:
    try:
        print('Введите значения')
        x = float(input('Первое число: x='))
        z = input('Введите операцию ("+", "-", "*", "/"):')
        y = float(input('Второе число: y='))
    except ValueError:
        print('\nВведено неверное значение! Попробуйте снова!')
    class_calc (x,z,y)
    i = int(input('Введите 1 для продолжения или 0 для выхода'))
