# Игра “Компьютер угадывает число”
# Пользователь загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у него “Твое число равно, меньше или больше чем число N?”,
# где N - число, которое хочет проверить компьютер.
# Пользователь отвечает одним из трех чисел: 1 - равно, 2 - больше, 3 - меньше
# Напишите программу, которая с помощью цепочки таких вопросов и ответов пользователя угадывает число

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за 7 попыток.

def AskQuestion(start_range, end_range):
    test_num = start_range+(end_range - start_range) // 2
    print(f'Ваше число {test_num}?')
    answer = int(input('Введите  1 - равно, 2 - больше, 3 - меньше: '))
    if answer == 1:
        start_range, end_range = -1, test_num
    elif answer == 2:
        start_range=test_num
    elif answer == 3:
        end_range = test_num
    else:
        print('Ваш ответ непонятен.')

    return [start_range, end_range]


start_range = 1
end_range = 100
work = True
while work:
    start_range, end_range =AskQuestion(start_range, end_range)
    if start_range == -1:
        print('Загаданное число: ', end_range)
        break
