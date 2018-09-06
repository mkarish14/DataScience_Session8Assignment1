
# coding: utf-8

# In[23]:


import pandas as pd

ser = pd.Series([7, 2, 0, 3, 4, 2, 5, 0, 3, 4])

Y= (ser.groupby(ser.eq(0).cumsum().mask(ser.eq(0))).cumcount() + 1).mask(ser.eq(0), 0).tolist()
print(Y)


# In[32]:


import numpy as np
dateindex = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(dateindex)), index=dateindex)
print(s)


# In[27]:


s[dateindex.weekday == 2].sum() 


# In[30]:


s.resample('M').mean()


# In[31]:


s.groupby(pd.TimeGrouper('4M')).idxmax()

