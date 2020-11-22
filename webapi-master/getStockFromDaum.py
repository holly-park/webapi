import json
import requests 

url = 'http://finance.daum.net/api/market_index/days?page=1&perPage=100&market=KOSPI&pagination=true'
header={
    'Referer':'http://finance.daum.net/domestic/kospi',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
res = requests.get(url, headers = header)
rt_dict = json.loads(res.content)
print(rt_dict, rt_dict.keys())

import pandas as pd
print(rt_dict['data'][2])
df = pd.DataFrame(rt_dict['data'])
print(df)
