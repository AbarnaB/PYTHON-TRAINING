#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
req=requests.get('https://jsonplaceholder.typicode.com/todos')
json=req.json()
print(json[0:5])


# In[7]:


import pandas as pd
import io
import requests
url="https://jsonplaceholder.typicode.com/todos"
x=requests.get(url).content
y=pd.read_json(io.StringIO(x.decode('utf-8')))
y.head(7)


# In[10]:


import requests
url="https://jsonplaceholder.typicode.com/todos"
x=  { "userId": 10,  "title": "macaroni", "completed": False}
res=requests.post(url,json=x)
res.json()
res.status_code


# In[24]:


import requests
import json
url="https://jsonplaceholder.typicode.com/todos/10"
data={'id':10, 'userID':1,'address+pincode':'pondy 605004','completed':'True'}
headers={'Content-Type':'application/json; charset=UTF-8'}
res=requests.put(url,data=json.dumps(data), headers=headers)
print(res.status_code)
print(res.ok)
print(res.content)
print(res.text)
print(type(res.text))
print(res.url)
print(res.headers['Content-Type'])
print(res.encoding)


# In[27]:


import requests
url="https://jsonplaceholder.typicode.com/todos/7"
res=requests.delete(url)
res.json()
res.status_code

