import pandas as pd
from datetime import datetime, timedelta
import zipfile, io
import requests
      
s_date = datetime(2022,10,24)
datelist = []
for i in range(11):
    list_date = s_date + timedelta(days=-i*3)
    datelist.append(list_date)
start_urls=[]
for i in datelist:
    _date=i.strftime('%Y%m%d')
    date_=i.strftime('%d%m%Y')
    start_urls.append('https://cafef1.mediacdn.vn/data/ami_data/'+_date+'/CafeF.SolieuGD.'+date_+'.zip')

for url in start_urls:
    #print(url)
    response = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall("G:\DE\STOCKS")
    