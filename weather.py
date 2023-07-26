import requests


WEATHER_TOKEN = "2c87759a08f90fd10c30d2935827efcd"

def weather_app(chosen_city="Tomsk, RU", token=WEATHER_TOKEN) -> str:
    city = chosen_city
    print(city)
    city_id = 1
    appid = token
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        city_id = data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)
        pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()

        weather_data = "Погода: " + data['weather'][0]['description'] + "\n" + \
                       "Температура: " + str(data['main']['temp']) + "\n" + \
                       "Минимум: " + str(data['main']['temp_min']) + "\n" + \
                       "Максимум: " + str(data['main']['temp_max'])
    except Exception as e:
        print("Exception (weather):", e)
        weather_data = "Ошибка ввода города. Проверьте правильность написания города."
        pass
    return weather_data

