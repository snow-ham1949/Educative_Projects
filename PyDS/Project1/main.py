# Just to avoid unnecessary warnings, the lines belwo are helpful!
import warnings
warnings.simplefilter("ignore")

# Essential imports for data analysis for visualization 
import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# Imports for offline interactive plotting
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot,plot
import cufflinks as cf
cf.go_offline()

# Setting style and inline plotting
sns.set_style('whitegrid')
print("Success")

rbc = pd.read_csv('RBC.csv', index_col='Date') # Royal Bank of Canada
cibc = pd.read_csv('CIBC.csv', index_col='Date') # Canadian Imperial Bank of Commerce
bmo = pd.read_csv('BMO.csv', index_col='Date') # Bank of Montreal 
suncor = pd.read_csv('Suncor.csv', index_col='Date') # Suncor Energy Inc.
encana = pd.read_csv('Encana.csv', index_col='Date' ) # Encana Corp.
cnq = pd.read_csv('CNQ.csv', index_col='Date' ) # Canadian Natural Resource Ltd.
uso = pd.read_csv('USO.csv', index_col='Date') # United States Oil Fund LP (ETF)
wti = pd.read_csv('WTI.csv', index_col='Date') # WTI Oil price

tickers = ['RBC', 'CIBC', 'BMO', 'Suncor', 'Encana','CNQ']
bo = pd.concat([rbc, cibc, bmo, suncor, encana, cnq], axis=1, keys=tickers)

bo.columns.names = ['Entity','Stock']

print("Max close price")
max_stock = bo.xs(key='Close', axis=1,level='Stock').max()
print(max_stock)
print("\n Min close Price")
min_stock = bo.xs(key='Close', axis=1,level='Stock').min()
print(min_stock)

fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(10, 4))
sns.barplot(data=max_stock, ax=axes[0])
axes[0].set_ylim(0, 120)
axes[0].set_ylabel('Max_Stock_Price - $')

sns.barplot(data=min_stock, ax=axes[1])
axes[1].set_ylim(0, 120)
axes[1].set_ylabel('Min_Stock_Price - $')
plt.savefig(fname='max_min_stock')
plt.clf()

for tick in tickers:
    bo[tick]['Close'].plot(figsize=(10, 6),label=tick)
plt.legend(loc=1)
plt.savefig(fname='close_price_line_plot')
plt.clf()

fig, axes = plt.subplots(ncols=1, nrows=2, figsize=(10, 6), sharex=True)
wti[::-1].plot(ax=axes[0], ylim=(0,150))
uso['Close'].plot(ax=axes[1], ylim=(0, 150), label='USO Stock Close')
plt.legend(loc=1)
plt.savefig(fname='wit_vs_uso')
plt.clf()

plt.figure(figsize=(12,6))
encana['Close'].loc['2008-01-01':'2008-12-30'].rolling(30).mean().plot(label='Encana-30 Day Avg')
encana['Close'].loc['2008-01-01':'2008-12-30'].plot(label='Encana Close')
cnq['Close'].loc['2008-01-01':'2008-12-30'].rolling(30).mean().plot(label='CNQ-30 Day Avg')
cnq['Close'].loc['2008-01-01':'2008-12-30'].plot(label='CNQ Close')
plt.legend(loc=1)
plt.savefig(fname='Encana_and_cnq_rolling_mean')
plt.clf()

sns.heatmap(bo.xs(key='Close', level='Stock', axis=1).corr(), annot=True)
plt.savefig('heatmap')