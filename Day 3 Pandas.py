#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = [['Ayo', 10], ['Imran', 15], ['Chucks', 14]]

df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)


# In[3]:


#Create the pandas  DataFrame from the dictionary of array list 

#Example1

data = {'Name' : ['Ayo', 'Imran', 'Chucks'], 'Age' :[10, 15, 14]}

#create the pandas DataFrame from the list and adding column headers

df = pd.DataFrame(data)

#print DataFrame
print(df)


# In[5]:


#Example 2

#Population and area (km/square) of some states in Nigeria and their capital

dict_data = {"State": ["Abia", "Adamawa", "Lagos", "Osun", "Rivers"], 
             "Capital": ["Umuahia", "Yola", "Ikeja", "Osogbo", "Portharcourt"], 
             "Area": [6320, 36917, 3345, 9251, 11077],
             "Population": [284627, 1274682, 736718, 482912, 647382]}

df = pd.DataFrame(dict_data)

print(df)


# In[13]:


csv_df = pd.read_csv('Desktop/Sensor2021.csv') 
print(csv_df)


# In[ ]:


#End of Day 3 Program


# In[ ]:


#Thanks

