import requests


def get_weather():
    city = input("Введите название города: ")
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lang=ru&q=\n'
                       f'{city}&appid=6798dc14c6cc12c2b890b267ff82341d&units=metric')
    data = res.json()

    if res.status_code == 200:
        print(f'погода в {city}:', data['weather'][0]['description'])
        print(f'температура: {data["main"]["temp"]} по Цельсию')
        print(f'давление: {data["main"]["pressure"]} гекто-паскаль')
        print(f'влажность: {data["main"]["humidity"]}%')

    else:
        print("Error", data)


def pochta():
    url = 'https://tracking.pochta.ru/tracking.json'
    params = {'barcode': 'RB123456789CN'}
    headers = {'Authorization': 'Bearer Тут должен быть API ключ'}

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if response.status_code == 200:
        print('Трек-номер:', data['trackingItem']['barcode'])
    else:
        print("Error", data)


get_weather()
