# 7.3. Введите в программу свой год рождения, и напишите код, который определит, високосный ли это год.
print('Задачка №7.3')
year = int(input('Введите свой год рождения: '))
# высокосный год начинается с 1600 года, кратен четырем годам, кратен четырехстам годам но не кратен 100 годам
if (year >= 1600 and year % 4 == 0 or (year % 100 != 0 and year % 400 == 0)):
    print('Вы родились в высокосный ', year, ' год.')
else:
    print('Вы родились в обычный (невысокосный) ', year, ' год.')
print('*' * 40)

# 7.4. Введите целое число и напечатайте, чётное ли оно.
print('Задачка №7.4')
num = int(input('Введите целое число: '))
if (num % 2 == 0):
    print('Введенное число четное. ')
else:
    print('Введенное число нечетное. ')
print('*' * 40)

# 7.5. Три бандита, Джек, Джон и Джун, никак не могут разобраться с награбленным. Каждый из них утащил несколько
# ящиков с золотом, и теперь они ругаются, кому же было тяжелее всего.
# Введите три числа и напечатайте "all equals" если все числа равны, "all different" если все числа различны, и
# "equal or different" в противном случае.
print('Задачка №7.5')
Jack = int(input('Сколько Джек схватил сундуков? '))
Jhon = int(input('Сколько сундуков упер Джон? '))
Jun = int(input('Джуну сколько досталось сундуков?'))
if (Jack == Jhon == Jun):
    print('all equals')
elif (Jack != Jhon and Jack != Jun and Jhon != Jun):
    print('all different')
else:
    print('equal or different"')
print('*' * 40)

# 7.6. После глобальной блокировки интернета стало невозможным быстро нагуглить, сколько в каком месяце дней,
# а многие даже стали путать весну и осень.
# Напишите программу, которая при вводе номера месяца 1..12 выводит количество дней в нём, а также соответствующий
# сезон года (один из четырёх).
print('Задачка №7.6')
month = int(input('Введите номер месяца 1..12: '))
ears_dict = dict(
    [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 30), (11, 30), (12, 31)])
# список, где ключ- номер месяца, значение - количество дней в этом месяце
print('В указанном месяце: ', ears_dict[month], ' дней.')
print('*' * 40)

# 7.8. Зомби захватывают мир! Вам срочно надо перепрошить бластер, чтобы мгновенно отличать зомби от нормального
# человека по его идентификационному номеру HID, который высвечивается на сенсорном экране.
#
# HID человека отличается тем, что делится без остатка и на 5 и на 11.
# Срочно перепрошейте свой бластер!
print('Задачка №7.8')
import random
print('Наступила осень и люди стали заболевать, но под рукой есть бластер с пилюлями от насморка...')
battery = 100  # количество зарядов в процентах
while (battery > 0):
    HID_human = random.randint(1, 10000)  # генератор встречных персонажей
    if (HID_human % 5 == 0 and HID_human % 11 == 0):
        print('Вижу кого то с HID: ', HID_human, ' Стрелять не буду, это пока ещё человек...')
    else:
        battery = battery - 10
        print('Вот выскочил кто то с HID: ', HID_human, ' Уже не человек, пожалуй можно и шмальнуть')
        print('Заряда осталось: ', battery, ' %')
print('Упс, батарейка села...')
print('Апчииии...')
print('*' * 40)
