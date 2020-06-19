from newsapi import NewsApiClient
from discord_webhooks import DiscordWebhooks
import schedule
import time

def job():
    url = 'add-your-webhook-url-here'
    newsapi = NewsApiClient(api_key='add-your-api-key-here')

    data = newsapi.get_top_headlines(language='en',country='in')

    if data['status'] == 'ok':
        ar1t = data['articles'][0]['title']
        ar1d = data['articles'][0]['url']
        ar1i = data['articles'][0]['urlToImage']

        ar2t = data['articles'][1]['title']
        ar2d = data['articles'][1]['url']
        ar2i = data['articles'][1]['urlToImage']

        ar3t = data['articles'][2]['title']
        ar3d = data['articles'][2]['url']
        ar3i = data['articles'][2]['urlToImage']

        ar4t = data['articles'][3]['title']
        ar4d = data['articles'][3]['url']
        ar4i = data['articles'][3]['urlToImage']

        ar5t = data['articles'][4]['title']
        ar5d = data['articles'][4]['url']
        ar5i = data['articles'][4]['urlToImage']

        cnews1 = DiscordWebhooks(url)
        cnews1.set_author(name="Today's top headlines")
        cnews1.set_content(title=ar1t,url=ar1d)
        cnews1.set_thumbnail(url=ar1i)

        cnews2 = DiscordWebhooks(url)
        cnews2.set_content(title=ar2t,url=ar2d)
        cnews2.set_thumbnail(url=ar2i)

        cnews3 = DiscordWebhooks(url)
        cnews3.set_content(title=ar3t,url=ar3d)
        cnews3.set_thumbnail(url=ar3i)

        cnews4 = DiscordWebhooks(url)
        cnews4.set_content(title=ar4t,url=ar4d)
        cnews4.set_thumbnail(url=ar4i)

        cnews5 = DiscordWebhooks(url)
        cnews5.set_content(title=ar5t,url=ar5d)
        cnews5.set_thumbnail(url=ar5i)
        cnews5.set_footer(text='Source - newsapi.org')

        cnews1.send()
        cnews2.send()
        cnews3.send()
        cnews4.send()
        cnews5.send()

    else:
        cnews = DiscordWebhooks(url)
        cnews.set_content(title="Sorry, we will be back soon with live news!")
        cnews.send()


schedule.every().day.at("07:30").do(job)
schedule.every().day.at("08:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



