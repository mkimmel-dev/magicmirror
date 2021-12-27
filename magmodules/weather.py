import os
from pyowm import OWM
import json
from datetime import datetime
from datetime import date
import calendar


weatherkey = '52ef17c768bee3262accfbd50ce1b6ee'
location = 'washington, d.c., us'


def converter(num):
    f = (num - 273.15) * (9/5) + 32
    return f


def get_weather():
    owm = OWM(weatherkey)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(location).to_dict()

    weathData = {}
    weathData['status'] = observation['weather']['detailed_status']
    weathData['temp'] = converter(observation['weather']['temperature']['temp'])

    return weathData

def get_forecast():
    owm = OWM(weatherkey)
    mgr = owm.weather_manager()

    oneClient = mgr.one_call(lat = 38.8776, lon = 77.0910)

    rawdata = [i.__dict__ for i in oneClient.forecast_daily]
    keyed = {}

    for day in rawdata:
        keyed[day['ref_time']] = day

    sortdict = dict(sorted(keyed.items(), key = lambda item: item[0]))
    sortday = [x for x in sortdict.values()]


    print(json.dumps(sortday))
    forecast = []
    for i in sortday:
        temp = {}
        temp['day'] = calendar.day_name[datetime.fromtimestamp(i['ref_time']).weekday()]
        temp['status'] = i['status']
        temp['avg'] = kelvcon(i['temp']['feels_like_day'])
        temp['high'] = kelvcon(i['temp']['max'])
        temp['low'] = kelvcon(i['temp']['min'])
        temp['humidity'] = f'{i["humidity"]}%'

        forecast.append(temp)
        
    print(forecast)

def kelvcon(x):
    return int((x - 273.15) * (9/5) + 32)


if __name__ == '__main__':
    get_forecast()






