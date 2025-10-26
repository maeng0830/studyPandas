import numpy as np
import pandas as pd
import FinanceDataReader as fdr

pd.set_option('display.float_format', lambda x: '%.2f' % x)

samsung_df = fdr.DataReader('005390', '2009-01-01', '2017-12-31')
kodex_df = fdr.DataReader('069500', '2009-01-01', '2017-12-31')

print(samsung_df)
#             Open  High   Low  Close   Volume  Change
# Date
# 2013-07-12  1130  1165  1120   1140  2089214     NaN
# 2013-07-15  1140  1140  1090   1095  3338789   -0.04
# 2013-07-16  1085  1120  1075   1095  1809329    0.00
# 2013-07-17  1110  1135  1090   1120  1340113    0.02
# 2013-07-18  1120  1120  1095   1100   982275   -0.02
# ...          ...   ...   ...    ...      ...     ...
# 2017-12-21  1080  1095  1050   1050   526785   -0.03
# 2017-12-22  1050  1065  1040   1050   575426    0.00
# 2017-12-26  1050  1070  1045   1060   441204    0.01
# 2017-12-27  1080  1095  1060   1095   428161    0.03
# 2017-12-28  1095  1095  1050   1065   559604   -0.03
#
# [1097 rows x 6 columns]
print(kodex_df)
#              Open   High    Low  Close    Volume  Change
# Date
# 2013-08-01  19697  19834  19560  19736   4963571     NaN
# 2013-08-02  19835  19927  19751  19833   6183490    0.00
# 2013-08-05  19773  19838  19710  19725   5807325   -0.01
# 2013-08-06  19688  19688  19443  19537   6870425   -0.01
# 2013-08-07  19397  19450  19247  19260   6624809   -0.01
# ...           ...    ...    ...    ...       ...     ...
# 2017-12-21  27491  27539  27025  27035   9653475   -0.02
# 2017-12-22  27101  27216  27032  27168   9562928    0.00
# 2017-12-26  27212  27375  27045  27055   8571867   -0.00
# 2017-12-27  27135  27366  27080  27375  14266892    0.01
# 2017-12-28  27378  27734  27374  27718   8524131    0.01
#
# [1083 rows x 6 columns]

############################################################
# concat은 DataFrame 또는 Series를 수평적 또는 수직적 연결할 수 있는 함수이다.
# 연결의 기준은 index 또는 columns

## axis=0
print(pd.concat([samsung_df, kodex_df[['Open', 'High']]]).head(2))
#             Open  High     Low   Close     Volume  Change
# Date
# 2013-07-12  1130  1165 1120.00 1140.00 2089214.00     NaN
# 2013-07-15  1140  1140 1090.00 1095.00 3338789.00   -0.04
print(pd.concat([samsung_df, kodex_df[['Open', 'High']]]).tail(2))
#              Open   High  Low  Close  Volume  Change
# Date
# 2017-12-27  27135  27366  NaN    NaN     NaN     NaN
# 2017-12-28  27378  27734  NaN    NaN     NaN     NaN

print(pd.concat([samsung_df, kodex_df], keys=['삼성', 'KODEX200'], names=['종목명']))  # multi index
#                       Open   High    Low  Close    Volume  Change
# 종목명      Date
# 삼성       2013-07-12   1130   1165   1120   1140   2089214     NaN
#          2013-07-15   1140   1140   1090   1095   3338789   -0.04
#          2013-07-16   1085   1120   1075   1095   1809329    0.00
#          2013-07-17   1110   1135   1090   1120   1340113    0.02
#          2013-07-18   1120   1120   1095   1100    982275   -0.02
# ...                    ...    ...    ...    ...       ...     ...
# KODEX200 2017-12-21  27491  27539  27025  27035   9653475   -0.02
#          2017-12-22  27101  27216  27032  27168   9562928    0.00
#          2017-12-26  27212  27375  27045  27055   8571867   -0.00
#          2017-12-27  27135  27366  27080  27375  14266892    0.01
#          2017-12-28  27378  27734  27374  27718   8524131    0.01
#
# [2180 rows x 6 columns]

## axis=1
print(pd.concat([samsung_df, kodex_df], axis=1).head(2))
#             Open  High   Low  Close   Volume  ...  High  Low  Close  Volume  Change
# Date                                          ...
# 2013-07-12  1130  1165  1120   1140  2089214  ...   NaN  NaN    NaN     NaN     NaN
# 2013-07-15  1140  1140  1090   1095  3338789  ...   NaN  NaN    NaN     NaN     NaN
#
# [2 rows x 12 columns]
print(pd.concat([samsung_df, kodex_df], axis=1, keys=['삼성', 'KODEX200']).head(2))  # multi column
#               삼성                             ... KODEX200
#             Open  High   Low Close   Volume  ...     High Low Close Volume Change
# Date                                         ...
# 2013-07-12  1130  1165  1120  1140  2089214  ...      NaN NaN   NaN    NaN    NaN
# 2013-07-15  1140  1140  1090  1095  3338789  ...      NaN NaN   NaN    NaN    NaN
#
# [2 rows x 12 columns]

## join은 concat 기준의 axis말고, 다른 axis에 대해서는 어떻게 join할 것인지 지정
print(pd.concat([samsung_df, kodex_df], keys=['삼성', 'kodex'], axis=1, names=['종목명']).head())  # default=outer
print(pd.concat([samsung_df, kodex_df[['Close']]], keys=['상성', 'kodex'], names=['종목명'], join='inner'))
#                   Close
# 종목명   Date
# 상성    2013-07-12   1140
#       2013-07-15   1095
#       2013-07-16   1095
#       2013-07-17   1120
#       2013-07-18   1100
# ...                 ...
# kodex 2017-12-21  27035
#       2017-12-22  27168
#       2017-12-26  27055
#       2017-12-27  27375
#       2017-12-28  27718
#
# [2180 rows x 1 columns]