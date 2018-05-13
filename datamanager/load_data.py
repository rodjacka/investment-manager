
from .models import Security, SecurityDailyPrice
import requests
import datetime


class DataWrangler():


    def load_data(self):
        securities_to_load = Security.objects.filter(fetch_data=True).all()
        for security in securities_to_load:
            self.get_data(security.symbol)

    def get_data(self, symbol):

        security = Security.objects.filter(symbol=symbol).all()[0]
        print(security.symbol)

        try:
            max_date = SecurityDailyPrice.objects.filter(security=security).latest('date').date
        except:
            max_date = datetime.date(1900,1,1)
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Referer': 'https://www.asx.com.au/prices/charting/?code=AAA&compareCode=&chartType=&priceMovingAverage1=&priceMovingAverage2=&volumeIndicator=&volumeMovingAverage=&timeframe=',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive'
        }
        url = 'https://www.asx.com.au/asx/1/chart/highcharts?asx_code={}&complete=true'.format(symbol)

        r = requests.get(url, headers=headers)
        if type(r.json()) == list:
            records = r.json()

            for r in records:
                trade_date = datetime.datetime.fromtimestamp(r[0]/1000)
                if trade_date.date() > max_date:
                    print('Saving {} {}'.format(symbol, str(trade_date)))
                    daily_price = SecurityDailyPrice(
                        security =security,
                        date   = trade_date,
                        open   = r[1],
                        high   = r[2],
                        low    = r[3],
                        close  = r[4],
                        volume = r[5]

                    )
                    daily_price.save()
        else:
            print("Error")


