#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

#Rows represent observations while columns represent input features


# In[13]:


data = [['Ayo', 10], ['Imran', 15], ['Chucks', 14]]

df = pd.DataFrame(data, columns = ['Name', 'Age'])
df


# In[14]:


#Create the pandas  DataFrame from the dictionary of array list 

#Example1

data = {'Name' : ['Ayo', 'Imran', 'Chucks'], 'Age' :[10, 15, 14]}

#create the pandas DataFrame from the list and adding column headers

df = pd.DataFrame(data)

#print DataFrame
df


# In[15]:


#Example 2

#Population and area (km/square) of some states in Nigeria and their capital

dict_data = {"State": ["Abia", "Adamawa", "Lagos", "Osun", "Rivers"], 
             "Capital": ["Umuahia", "Yola", "Ikeja", "Osogbo", "Portharcourt"], 
             "Area": [6320, 36917, 3345, 9251, 11077],
             "Population": [284627, 1274682, 736718, 482912, 647382]}

df = pd.DataFrame(dict_data)

df


# In[83]:


csv_df = pd.read_csv('Desktop/Sensor2021.csv') 
print(csv_df)


# In[84]:


csv_df.describe()


# In[25]:


csv_df['POPULATION'].mean()


# In[28]:


csv_df['POPULATION'].median()


# In[29]:


csv_df['POPULATION'].std()


# In[30]:


csv_df['POPULATION'].min()


# In[31]:


csv_df['POPULATION'].max()


# In[32]:


csv_df.columns


# In[38]:


csv_df.info()


# In[85]:


print("This is State Column as Pandas Series", '\n')


print(csv_df ['STATES'], '\n')



print("This is State Column as Pandas Dataframe", '\n')

print(csv_df [['STATES']], '\n')


#This print out DataFrame with States and Population Columns"

print("This is DataFrame with States and Population Column", '\n')


print(csv_df [['STATES', 'POPULATION']])


# In[89]:


print(csv_df[0:10], '\n')

print(csv_df[10:16])
      


# In[155]:


#Using loc and Iloc
#Since the dataset contains no label-based index, we can only use integer based ioc

#Print out observation for the third state
print(csv_df.iloc[2], '\n' '\n')

#Print out observation for the 4th and 5th state
print(csv_df.loc[[3, 4]])


# In[189]:


df = csv_df.drop(["CAPITAL"], axis =1)
print(csv_df)


# In[215]:


df['AREA POPULATION'] = df['AREA(km2)'] + df['POPULATION']
df.columns


# In[212]:


df.sort_index(inplace = True, ascending = True)

df


# In[219]:


df = csv_df.drop(["AreaPopulation"], axis =1)
df


# In[ ]:




