#%%
#Import relavent data
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

#%%
# Load data
epex_data = pd.read_csv('epex_day_ahead_price.csv')
spot_data = pd.read_csv('spot_intraday_price.csv')
system_data = pd.read_csv('systemprice.csv')

#%%
#Convert time
start_date = datetime(year = 2019, month = 3, day = 31, hour = 23, minute = 00)
delta_t = timedelta(minutes=30)
epex_date = []
epex_date.append(start_date)
for i in range(1, len(epex_data['timestamp'])):
    new_date = epex_date[i-1] + delta_t
    epex_date.append(new_date)

#%%
#Group by date
epex_data['Date'] = epex_date
# epex_data.set_index("Date",inplace=True)
#%%
# Analyzed data
print(epex_data.head(5))
print(spot_data.head(5))
print(system_data.head(5))
#%%
# Plot data
mean_data = epex_data.groupby(pd.Grouper(key = 'Date', freq = '7D')).mean()
#%%
plt.plot(mean_data['Date'],mean_data['apx_da_hourly'])
plt.show()
# %%
day = 48
week = 336

mi=-337
ma=mi + week 
data = epex_data[mi:ma]

# %%
plt.plot(data['timestamp'], data['apx_da_hourly'])
# %%
