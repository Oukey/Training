print('Задачка №7.1')
'''
7.1. В вашем отделе работают три программиста -- джун, миддл и сеньор. При этом не обязательно зарплата сеньора
самая высокая. Введите в программу три числа (зарплаты) и определите, у кого она самая высокая, у кого самая низкая,
и во сколько раз самая большая отличается от самой маленькой.
'''
import operator  # для определения ключа с максимальным значением

salary_Junior = int(input('Назначьте зарплату Джуну: '))
salary_Middle = int(input('Назначьте зарплату Миддлу: '))
salary_Senior = int(input('Определите вознаграждение Сеньора: '))

group = {'Junior': salary_Junior, 'Middle': salary_Middle, 'Senior': salary_Senior}
top = max(group.items(), key=operator.itemgetter(1))[0]  # Определение ключа словаря по макс. значению
no_top = min(group.items(), key=operator.itemgetter(1))[0]  # Определение ключа словаря по мин. значению
max_salary = int(max(salary_Junior, salary_Middle, salary_Senior))
min_salary = min(salary_Junior, salary_Middle, salary_Senior)
ratio = max_salary / min_salary

print('Самой высокой зарплаты достоин ', top)
print('Его зарплата больше чем у ', no_top, ' в ', round(ratio, 2), ' раза')
print('*' * 40)

print('Задачка №7.2')
'''
Ваш фрегат электронно-технического дозора в ходе разведки плутониевых залежей в галактике Tama обнаружил вражеское
транспортное судно и включил скрамблер, чтобы заблокировать возможность его побега. Но для этого вам придётся проявить
максимум мастерства, чтобы удерживать скорость противника в очень узком диапазоне.
Введите два вещественных числа и проверьте, совпадают ли они с точностью до третьего знака после запятой включительно.
'''
num_a = float(input(' Введите первое значение: '))
num_b = float(input(' Введите второе значение: '))
if (round(num_a, 3) == round(num_b, 3)):
    print(round(num_a, 3), '==', round(num_b, 3))
    print('Значения равны, с точностью до третьего знака после запятой')
else:
    print('Указанные значения не равны!')
    print(round(num_a, 3), '!=', round(num_b, 3))
print('*' * 40)

print('Задачка №7.7')
'''
7.7. Очень подозрительная фирма неожиданно выиграла подряд на покраску домов в городе. Красятся только четыре стены и
только снаружи. Все дома сделаны по типовому проекту -- размер каждой стены W метров в ширину по одной стороне, L
метров в ширину по другой стороне, и H метров в высоту. На покраску случайным образом поступают банки одного из двух
типов -- объёмом, достаточным для покраски 15 кв.м. и объёмом на 42 кв.м. Заранее неизвестно, какой вид краски прибудет.
Имеются небезосновательные подозрения, что существенная часть краски сбывается налево.
Ваша задача как общественного инспектора проверить, сколько минимально банок краски требуется для конкретной модели дома.
Входные данные, четыре числа:
объём банки краски (15 или 42 или любое другое)
размеры стены (W L H)
'''
bank_size = int(input('Укажите площадь окрашиваемой поверхности одной банки: '))
length = float(input('Длина стены в метрах: '))
width = float(input('Ширина стены в метрах: '))
height = float(input('высота стены стены в метрах: '))
wall_area = (length + width) * 2 * height  # Расчет площади стен дома
sum = wall_area / bank_size

print('Для окрашивания стен дома, с указанными размерами необходимо минимум: ', round(sum, 2),
      ' банок краски(без учета дверных и оконных проемов)')
print('*' * 40)

print('Задачка №7.9')
'''
Напишите программу, которая вычисляет возраст пёсика как если бы он был человеком. По "человечески" собачий возраст
считается так: первые два года реального возраста пса идут по 10.5 человечьих лет каждый, а каждый следующий --
по 4 человеческих года.
'''
dog_age = int(input('Сколько песику лет? '))
man_age = 0
if (dog_age <= 2):
    man_age = dog_age * 10.5
else:
    man_age = 2 * 10.5 + (dog_age - 2) * 4
print('В переводе на человеческий получается: ', int(man_age), 'лет(года)')

print('*' * 40)

print('Задачка №7.10')  # Задача была решена мной ранее, код практически без изменений
print('Расчет совместимости по году рождения.')
your_age = int(input('Ваш год рождения:'))
his_age = int(input('Его год рождения: '))
your_result = 0
ist_result = 0
if 1900 < his_age < 2100:
    while your_age > 0:
        your_result = your_result + your_age % 10
        your_age = your_age // 10
    while his_age > 0:
        ist_result = ist_result + his_age % 10
        his_age = his_age // 10
    print('Сумма твоего года рождения: ', your_result, ' сумма его года рождения: ', ist_result)
    if your_result > ist_result:
        print('Он тебе подходит!!!')
    else:
        print('Он тебе не пара')
else:
    print('У вас очень большая разница в возрасте')