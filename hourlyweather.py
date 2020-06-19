
from discord_webhooks import DiscordWebhooks
import requests
import schedule
import time

def job():
    url = 'add-your-webhook-url-here'
    apiurl = 'add-your-api-url-here'
    res = requests.get(apiurl)
    data = res.json()

    # current weather data extract
    ctemp = data['current']['temp']
    cwspeed = data['current']['wind_speed']
    ccloud = data['current']['clouds']
    cwmain = data['current']['weather'][0]['main']
    cwdesc = data['current']['weather'][0]['description']
    cicon = data['current']['weather'][0]['icon']

    #int to string and some calculations
    c_temp = str(ctemp)
    c_clouds = str(ccloud)
    c_wspeed = str(cwspeed)
    #h_temp = str(htemp)
    #h_clouds = str(hcloud)

    # message design for current weather
    cweather = DiscordWebhooks(url)
    cweather.set_content(title="Current Weather")
    cweather.set_thumbnail(url='http://openweathermap.org/img/wn/'+ cicon + '@4x.png')
    cweather.add_field(name='Temperature :', value=str(c_temp + " ºC"))
    cweather.add_field(name='Wind speed :', value=str(c_wspeed + " km/h"))
    cweather.add_field(name=(cwmain + ' :'), value=cwdesc)
    cweather.add_field(name='Cloudiness :', value=(c_clouds + '%'))
    cweather.set_footer(text='Source - OpenWeather')

    cweather.send()

# scheduling script to send messages
schedule.every().day.at("06:05").do(job)
schedule.every().day.at("07:05").do(job)
schedule.every().day.at("08:05").do(job)
schedule.every().day.at("09:05").do(job)
schedule.every().day.at("10:05").do(job)
schedule.every().day.at("11:05").do(job)
schedule.every().day.at("12:05").do(job)
schedule.every().day.at("13:05").do(job)
schedule.every().day.at("14:05").do(job)
schedule.every().day.at("15:05").do(job)
schedule.every().day.at("16:05").do(job)
schedule.every().day.at("17:05").do(job)
schedule.every().day.at("18:05").do(job)
schedule.every().day.at("19:05").do(job)
schedule.every().day.at("20:05").do(job)
schedule.every().day.at("21:05").do(job)
schedule.every().day.at("22:05").do(job)
schedule.every().day.at("23:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

