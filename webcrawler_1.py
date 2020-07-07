#!/usr/bin/env python
# coding: utf-8

# In[32]:


# -*- coding: 'utf-8' -*-
import requests
city = 1
while city:
    city = input('请输入城市，回车退出：')
    r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s'%city)
    data_w = r.json()
    try:
        dict_w = data_w['data']
        print(data_w)
        f = dict_w['forecast'][0]
        date = f['date']
        high = f['high']
        low = f['low']
        t = f['type']
        print('%s\n%s\n高温 %s\n低温 %s\n天气%s\n'%(city, date, high, low, t))
    except:
        print('未获得')
    
print('退出程序')


# In[ ]:




