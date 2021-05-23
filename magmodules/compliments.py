import os
from pyowm import OWM
import datetime
import random
weatherkey = os.environ['WEATHER']
location = os.environ['LOCATION']

compliments = {
  "day": {
    "compliments": [
      "looks like it'll be a good day!",
      "hey there!",
      "lookin good!",
      "get after it!",
      "go get some tacos",
      "how\u0027s Stitch doing?",
      "hungry for lunch?",
      "Yo!"
    ]
  },
  "morning":{
    "compliments": [
        "looking good!",
        "have a good day!",
        "you're gonna kill it!",
        "get after it!"
    ]
  },
  "afternoon": {
    "compliments": [
      "how was work?",
      "traffic bad?",
      "nice to see you again",
      "grab a beer!",
      "go chill!",
      "wanna play games?"
    ]
  },
  "night":{
    "compliments":[
        "time to rest",
        "ready for tomorrow?",
        "check out what's new on netflix!",
        "cuddle up!",
        "get cozy!",
        "sweatpants time!",
        "how was dinner?"
    ]
  },
  "clouds": {
    "compliments": [
      "don't forget your umbrella!",
      "kinda grey today",
      "there's sun behind there somewhere"
    ]
  },
  "sun": {
    "compliments": [
      "lookin like a good day to tan",
      "is the pool open?",
      "don't get burned!"
    ]
  },
  "fog": {
    "compliments": [
        "drive safe!",
        "lookout for zombies!"
     ]
  },
  "rain":{
    "compliments":[
        "drive safe!",
        "don't forget your umbrella!",
        "got a rainjacket?",
        "make sure your wipers work!"
    ]
  },
  "storm":{
    "compliments":[
        "watch out for lightning!",
        "how's the thunder?",
        "sun should be out after this",
        "stay dry!"
    ]
  }
}

def get_compliment():
    currentweather = ""

    owm =OWM(weatherkey)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(location)
    w = observation.weather.__dict__



    currentweather = w['status'].lower()
    hour = datetime.datetime.now().hour
    validTimes = timeValidator(hour)



    timeList = []
    weatherList = compliments[currentweather]['compliments']
    for i in validTimes:
        timeList.extend(compliments[i]['compliments'])

    complimentList = [*timeList, *weatherList]

    return random.choice(complimentList)


def timeValidator(hour):
    timeconfig = {
        'morning' : [4,12],
        "afternoon" : [12,18],
        'night' : [18,24],
        'day': [4,18],
    }

    validTimes = []
    for i in timeconfig.items():
        if min(i[1]) <= hour and max(i[1]) >= hour:
            validTimes.append(i[0])

    return validTimes

