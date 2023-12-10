#!/usr/bin/env python
# coding: utf-8

# In[72]:


## Spotify Data Analysis


# In[3]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install numpy')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')


# In[ ]:





# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


df_tracks = pd.read_csv('G:/spotify-dataset/tracks.csv')
df_tracks.head()


# In[12]:


# null values
pd.isnull(df_tracks).sum()


# In[14]:


#Check the Data Type and Memory Usage
df_tracks.info()


# In[19]:


#Ten Least Popular Songs
sorted_df = df_tracks.sort_values('popularity', ascending = True).head(10)
sorted_df


# In[20]:


df_tracks.describe().transpose()


# In[21]:


#Top Ten Popular Songs With Popularity More Than 90.
most_popular = df_tracks.query('popularity>90', inplace = False).sort_values('popularity',ascending = False)
most_popular[:10]


# In[ ]:


#Make the Release Date Column as the Index Column
df_tracks.set_index('release_date', inplace = True)
df_tracks.index=pd.to_datetime(tracks.index)
df_tracks.head()


# In[36]:


# Name of the Artist Present in the 18th Row of the Dataset
df_tracks[["artists"]].iloc[18]


# In[37]:


#Duration of the Songs From Milliseconds to Seconds.
df_tracks["duration"]=df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms",inplace=True,axis=1)


# In[38]:


df_tracks.duration.head()


# In[ ]:


#correlation map
corr = df_tracks.drop(['key','mode','explicit'], axis=1).corr(method = 'pearson')
plt.figure(figsize=(14,6))
map = sns.heatmap(cm, annot = True, fmt = '.1g', vmin=-1, vmax=1, center=0, cmap='inferno', linewidths=1, linecolor='Black')
map.set_title('Correlation Heatmap between Variable')
map.set_xticklabels(map.get_xticklabels(), rotation=90)


# In[54]:


#Let’s Move Ahead and Sample Only 4 Percent of the Whole Dataset.
sample_df = df_tracks.sample(int(0.004 * len(df_tracks)))
len(sample_df)


# In[55]:


#Regression line_loudness and energy
plt.figure(figsize=(10,6))
sns.regplot(data=sample_df, y='loudness', x='energy', color='c').set(title='Loudness vs Energy Correlation')


# In[56]:


#Regression line - popularity and acousticness
plt.figure(figsize=(10,6))
sns.regplot(data=sample_df, y='popularity', x='acousticness', color='b').set(title='Popularity vs Acousticness Correlation')


# In[63]:


#Data analysis based on genres of the song
df_artists=pd.read_csv('G:/spotify-dataset/artists.csv')
df_artists.head()

