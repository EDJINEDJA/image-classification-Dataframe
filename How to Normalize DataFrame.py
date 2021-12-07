#!/usr/bin/env python
# coding: utf-8

# In[8]:


#this function give us the normalisation of our data set if we want to normalize

import pandas as pd
import numpy as np

np.random.seed(0)

df = pd.DataFrame(np.random.randint(-100,100,size=(20, 4)), columns=list('ABCD')) #data generation

#Function

def mean_norm(df_input):
    return df_input.apply(lambda x: (x-x.mean())/ x.std(), axis=0)

df_mean_norm = mean_norm(df)


# In[ ]:




