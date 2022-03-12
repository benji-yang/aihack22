#%%
#Import relavent data
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

#%%
# Load data
epex_data = pd.read_csv('epex_day_ahead_price.csv')
spot_data = pd.read_csv('spot_intraday_price.csv')
system_data = pd.read_csv('systemprice.csv')

#%%
# Analyzed data
print(epex_data.head(5))
print(spot_data.head(5))
print(system_data.head(5))
#%%
# Plot data
plt.plot(epex_data['timestamp'], epex_data['apx_da_hourly'])
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
