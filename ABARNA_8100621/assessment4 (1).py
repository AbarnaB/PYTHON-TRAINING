#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
exl=pd.read_excel(r'C:\Users\ABU ANI\Downloads\nba.xlsx')
print(exl)


# In[7]:


import pandas as pd
exl1=pd.read_excel(r'C:\Users\ABU ANI\Downloads\matches.xlsx')
print(exl1)


# In[8]:


import pandas as pd
data = {'Name':['Jai', 'Prince', 'Gaurav', 'Anuj'],'Age':[27, 24, 22, 32],'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
print(df)


# In[10]:


import pandas as pd
data = {'Name':['Jai', 'Prince', 'Gaurav', 'Anuj'],'Age':[27, 24, 22, 32],'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
print(df)
Address=['Delhi', 'Kanpur', 'Allahabad', 'Mumbai']
df['Address']=Address
df


# In[12]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\nba.csv')
print(df)


# In[13]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\nba.csv')
res=df.head(5)
print("First 5 rows of the dataframe: ")
print(res)


# In[15]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\nba.csv')
print(df.shape)


# In[16]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\nba.csv')
print(df.dtypes)


# In[17]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\nba.csv')
print(df.describe)


# In[18]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\nba.csv')
print(df.median())


# In[19]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\nba.csv')
m=df['Age']
print(m.median())


# In[28]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\matches.csv')
df.info()


# In[30]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\matches.csv')
df.info()


# In[31]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\matches.csv')
m=df['win_by_wickets']
print(m.mean())


# In[33]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\matches.csv')
m=df['win_by_wickets']
print(m.std())


# In[35]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\matches.csv')
gb=df.groupby(["city","winner"]).count()
print(gb)


# In[42]:


import pandas as pd
df=pd.read_csv(r'C:\Users\ABU ANI\Downloads\matches.csv')


# In[43]:


df.groupby('winner').count()/len(df)


# In[44]:


df.groupby(['winner','city']).count()/df.groupby('winner').count()['city']

