import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell
import FinanceDataReader as fdr

pd.set_option('display.float_format', lambda x: '%.2f' % x)
InteractiveShell.ast_node_interactivity = "all"

samsung_df = fdr.DataReader('005390', '2017-01-01', '2017-12-31')
print(samsung_df.head())
#             Open  High   Low  Close   Volume  Change
# Date
# 2017-01-02  1260  1300  1255   1295  1232965    0.04
# 2017-01-03  1305  1315  1280   1310   886559    0.01
# 2017-01-04  1305  1310  1280   1305   446070   -0.00
# 2017-01-05  1305  1330  1300   1320   721691    0.01
# 2017-01-06  1320  1345  1305   1325   645608    0.00


# Stateful
x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x, y)
plt.show()

x = [-3, 5, 7]
y = [10, 2, 5]
plt.figure(figsize=(15, 3))
plt.plot(x, y)
plt.xlim(0, 10)
plt.ylim(-3, 8)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot')
plt.suptitle('Figure Title', size=10, y=1.05)
plt.show()

plt.plot(samsung_df.index, samsung_df['Close'])
plt.show()


