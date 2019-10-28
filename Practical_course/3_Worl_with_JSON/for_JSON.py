import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)
s = json.dumps(result, indent=1)

# Сохранение данных в json файл
with open("file_api.json", "wt") as file_api:
    json.dump(result, file_api, indent=1)


# Подсчет количества уникальных пользователей в наборе
def unique_users(res):
    ''' Функция определения уникальных пользователей '''
    user_list = []
    for i in range(len(res)):
        user_list.append(res[i].get('userId'))
    return set(user_list)


def get_len_users(res):
    '''Функция возвращает количество уникальных пользователей'''
    return len(unique_users(res))


def original_tasks(res):
    '''Функция возвращает словарь с выполненными заданиями по каждому пользователю'''
    summary = {}
    user_list = unique_users(res)
    for i in user_list:
        summary[i] = {'task': 0, 'completed': 0}
        for el in range(len(res)):
            if res[el]['userId'] == i:
                summary[i]['task'] += 1
                if res[el]['completed'] is True:
                    summary[i]['completed'] += 1
    return summary


user = original_tasks(result)
for i in user:
    print('Пользователь {}. Количество задач {} из них выполнено {}.'.format(i, user[i]['task'], user[i]['completed']))