import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell
import FinanceDataReader as fdr
from IPython.core.pylabtools import figsize

pd.set_option('display.float_format', lambda x: '%.2f' % x)
InteractiveShell.ast_node_interactivity = "all"

samsung_df = fdr.DataReader('005930', '2017-01-01', '2017-12-31')
print(samsung_df.head())
#             Open  High   Low  Close   Volume  Change
# Date
# 2017-01-02  1260  1300  1255   1295  1232965    0.04
# 2017-01-03  1305  1315  1280   1310   886559    0.01
# 2017-01-04  1305  1310  1280   1305   446070   -0.00
# 2017-01-05  1305  1330  1300   1320   721691    0.01
# 2017-01-06  1320  1345  1305   1325   645608    0.00

x = [-3, 5, 7]
y = [10, 2, 5]

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-3, 8)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Line Plot')
fig.suptitle('Figure Title', size=10, y=1.03)
fig.show()

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(samsung_df.index, samsung_df['Close'])
fig.show()


# figure, axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
print(type(fig))  # <class 'matplotlib.figure.Figure'>
print(type(axes))  # <class 'numpy.ndarray'>
print(axes)
# [[<Axes: > <Axes: >]
#  [<Axes: > <Axes: >]]
print(axes[0][0])
# Axes(0.125,0.53;0.352273x0.35)
print(axes[0][0].get_children())
# [<matplotlib.spines.Spine object at 0x000002AA7ED5E6C0>,
# <matplotlib.spines.Spine object at 0x000002AA7ED5F8F0>,
# <matplotlib.spines.Spine object at 0x000002AA7ED5EF60>,
# <matplotlib.spines.Spine object at 0x000002AA7ED7E5D0>,
# <matplotlib.axis.XAxis object at 0x000002AA7ED7EDE0>,
# <matplotlib.axis.YAxis object at 0x000002AA7ED5FE00>,
# Text(0.5, 1.0, ''), Text(0.0, 1.0, ''), Text(1.0, 1.0, ''),
# <matplotlib.patches.Rectangle object at 0x000002AA7ED7FD70>]

ax = axes[0][0]
print(ax.xaxis == ax.get_xaxis())  # True

# example
data = fdr.DataReader('005930', '2019-01-01', '2020-01-01')
close_series = data['Close']
print(close_series.head())
volume_series = data['Volume']
print(volume_series.head())

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), sharex=True)
ax1 = axes[0]
ax2 = axes[1]

ax1.plot(close_series.index, close_series, linewidth=2, linestyle='--', label='Close')
ax1.set_title('Samsung price', fontsize=10, family='Arial')
ax1.set_ylabel('price', fontsize=10, family='Arial')
ax1.set_xlabel('date', fontsize=10, family='Arial')
ax1.legend(loc='upper left')

ax2.bar(volume_series.index, volume_series, label='Volume')
ax2.set_title('Samsung volume', fontsize=10, family='Arial')
ax2.set_ylabel('volume', fontsize=10, family='Arial')
ax2.set_xlabel('date', fontsize=10, family='Arial')
ax2.legend(loc='upper left')

fig.suptitle('Samsung', fontsize=15, family='Verdana')
fig.show()
