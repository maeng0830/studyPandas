import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell
import FinanceDataReader as fdr

pd.set_option('display.float_format', lambda x: '%.2f' % x)
InteractiveShell.ast_node_interactivity = "all"

samsung_series = fdr.DataReader('005930', '2017-01-01', '2018-01-01')['Close']
kodex_series = fdr.DataReader('069500', '2017-01-01', '2018-01-01')['Close']

price_df = pd.concat([samsung_series, kodex_series], axis=1)
price_df.columns = ['삼성전자', 'KODEX 200']
print(price_df.head())
#              삼성전자  KODEX 200
# Date
# 2017-01-02  36100      21827
# 2017-01-03  36480      22000
# 2017-01-04  36160      22025
# 2017-01-05  35560      21938
# 2017-01-06  36200      22032

price_max_df = price_df.groupby(price_df.index.month).max()
print(price_max_df.head())
#        삼성전자  KODEX 200
# Date
# 1     39900      22634
# 2     39560      22846
# 3     42560      23743
# 4     44620      24148
# 5     47020      25889

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4))
price_max_df.plot(ax=ax1, kind='line')
price_max_df.plot(ax=ax2, kind='bar')
price_max_df.plot(ax=ax3, x='삼성전자', y='KODEX 200', kind='scatter')
fig.show()