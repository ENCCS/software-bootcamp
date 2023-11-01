#!/usr/bin/env python
# coding: utf-8

# In[2]:

import sys
import pandas as pd

url = "https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_tapiola.csv"
weather = pd.read_csv(url,comment='#')

# define the start and end time for the plot 
start_date=pd.to_datetime(sys.argv[1], dayfirst=True)
end_date=pd.to_datetime(sys.argv[2], dayfirst=True)

output_file_name = sys.argv[3]

# The date format in the file is in a day-first format, which matplotlib does nto understand.
# so we need to convert it.
weather['Local time'] = pd.to_datetime(weather['Local time'],dayfirst=True)
# select the data
weather = weather[weather['Local time'].between(start_date,end_date)]


# Now, we have the data loaded, and adapted to our needs. So lets get plotting

# In[4]:


import matplotlib.pyplot as plt
# start the figure.
fig, ax = plt.subplots()
ax.plot(weather['Local time'], weather['T'])
# label the axes
ax.set_xlabel("Date of observation")
ax.set_ylabel("Temperature in Celsius")
ax.set_title("Temperature Observations")
# adjust the date labels, so that they look nicer
fig.autofmt_xdate()
# save the figure

#fig.savefig('weather.png')
fig.savefig(sys.argv[3])

# In[ ]:




