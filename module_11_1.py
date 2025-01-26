'''
программа выводит график курса рубля к доллару на FOREX за прошедшую неделю.
Для получения данных через  API сервиса openexchangerates.org использован модуль requests.
Для отображения графика - модуль matplotlib.pyplot
'''

import requests
import datetime
import matplotlib.pyplot as plt


days = []  # массив дат прошедшей недели
t = datetime.datetime.now()
for i in range(7):
    days.append(t.strftime('%Y-%m-%d'))  # формат необходимый для запроса на API
    t += datetime.timedelta(days=-1)
days.reverse()

# начальный набор курсов рубля за неделю

cur = [1, 1, 1, 1, 1, 1, 1]

# обращаемся к ресурсу

with open('.env-11-1', 'r', encoding='UTF-8') as f:
    app_id = f.readline() #типа токен
headers = {"accept": "application/json"}

''' образец ответа
{
    disclaimer: "Usage subject to terms: https://openexchangerates.org/terms",
    license: "https://openexchangerates.org/license",
    timestamp: 1341936000,
    base: "USD",
    rates: {
        AED: 3.672914,
        AFN: 48.337601,
        ALL: 111.863334
        /* ... */
    }
}

'''
base = "USD"

for i, day in enumerate(days):
    url = f"https://openexchangerates.org/api/historical/{day}.json?app_id={app_id}"
    try:
        response = requests.get(url, headers=headers)

    except  Exception as e:
        print('request error')
        print(e)
    else:

        cur[i] = response.json()['rates']['RUB']
        base = response.json()['base']

# переформатируем дату чтобы лучше влезала на картинку
days = list(map(lambda day: day[5:].replace('-', '.'), days))

fig, ax = plt.subplots()  # Create a figure containing a single Axes.
ax.set_title(f"Курс рубля к {base} за прошедшую неделю")
ax.plot(days, cur)  # Plot some data on the Axes.
plt.show()  # Show the figure.
