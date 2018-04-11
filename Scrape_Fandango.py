
# coding: utf-8

# In[192]:


import json
import re

import requests
import scrapy


# In[193]:


headers = {'User-Agent': 'UNC Journo Class'}


# In[194]:


dur1init = requests.get('https://www.fandango.com/durham_+nc_movietimes', headers=headers)
body_str = dur1init.content.decode('utf-8')


# In[195]:


dur1 = requests.get('https://www.fandango.com/napi/theaterswithshowtimes?zipCode=&city=durham&state=nc&date=2018-04-11&page=1&favTheaterOnly=false&limit=10&isdesktop=true',headers=headers)
body_str = dur1.content.decode('utf-8')
#sel = scrapy.Selector(text=body_str)
#table = sel.css('body').xpath('string()').extract()
#table.json()
json_data = json.loads(dur1.text)
with open('durham1.json', 'w') as f:
    json.dump(json_data, f)

dur1init2 = requests.get('https://www.fandango.com/durham_+nc_movietimes?pn=2', headers=headers)
dur2 = requests.get('https://www.fandango.com/napi/theaterswithshowtimes?zipCode=&city=durham&state=nc&date=2018-04-11&page=1&favTheaterOnly=false&limit=10&isdesktop=true',headers=headers)
dur2.json()
with open('durham2.json', 'w') as f:
    json.dump(table, f)


# In[6]:


#sel = scrapy.Selector(text=body_str)


# In[7]:


#table = sel.css('table')[0]


# In[8]:


#table


# In[ ]:


to_dump = [p.copy() for p in players]
for p in to_dump:
    p.pop('sel')
    for k in list(p.keys()):
        if 'raw' in k:
            p.pop(k)
with open('scraped_players.json', 'w') as f:
    json.dump(to_dump, f)

