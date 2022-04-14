import requests
import os


def telegram_bot_sendtext(bot_message):
    bot_token = "1954038233:AAE41ANEN4rdlFsg-Gf_p2yzEK5FJphDyvo"
    bot_chatID = "72636178"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response_tg = requests.get(send_text)

    return response_tg.json()


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"

weather_params = {
    "lat": "40.378024",
    "lon": "49.827226",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
#
if will_rain:
    telegram_bot_sendtext("It's going to rain today. Remember to bring an ☔")
else:
    telegram_bot_sendtext("It is not going to rain today!")


# Environment variables
# If you go into your PyCharm project and you go into this tab where it says "Terminal", here if you type in env
# and hit "Enter", you can see a whole bunch of variables. So you've got a key and a value and in between
# there is just a single equal (=) sign. So these are the different variables that are set in the environment
# in which your code is run. These variables have values which are strings which can be used in
# our applications or our code. What exactly all these environment variables used for? Well,
# there's two major use cases.
# One is for convenience. Normally when you deploy a large application,
# the process is quite complicated. And once you've done it, you kind of don't want to mess around
# with the code base and update the code files like your main.py for example. Instead, you could have these
# environment variables, which you can change. For example, if you had an application that was sending you
# emails out to your clients, then your client base emails might change day to day. So certain variables that are
# being used in your code base could be set as environment variables and you can modify those
# variables without having to touch the code.
# A second reason might be for security. So when you're developing software, you might be uploading your code based
# somewhere, for example to store it online or to a service like PythonAnywhere. And it's usually not a good idea
# to have things like your authentication keys or your API keys to be stored in the same place as
# the rest of your code. That's where environment variables come in. So environment variables essentially allow
# us to separate out where we store our keys, our secret stuff, and various other variables away from where our code
# base is located. In our case, it doesn't really matter because we haven't got a paid account anywhere in here.
# It doesn't really matter if somebody steals our auth token or our API key, because none of those are linked to
# our payment details. Now, however, if we were to upgrade our accounts on open weather map's API or on Twilio's API,
# then we definitely want to keep these two things secret; auth token and the API key. Instead of having it located
# in the same place where we've got our code base which means you might accidentally upload it somewhere on
# the internet where other people can see it, instead, we can store these two things as environment variables.
# We can create an environment variable by simply typing export and then the name of the variable which I'll call
# OWM _API_KEY. And then it's really important that we have no spaces, but just a single equal sign.
# And then we're going to store everything that's in between the quotation marks.
