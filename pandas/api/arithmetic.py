import numpy as np
import pandas as pd
import FinanceDataReader as fdr

price_df = fdr.DataReader("005930", '2013-01-01', '2018-03-21')
df = pd.read_csv('../../my_data/naver_finance/2015_12.csv')

# axis
## numpy-axis
# 차원  축 번호  의미(방향)                  예: sum(axis=?)가 "무엇"을 합치는가
# ----  ------  ---------------------------  --------------------------------------------
# 1D    없음    길이 방향(유일한 축)         전체 원소를 하나로 합침 (스칼라)
# 2D     0      아래 방향(행을 따라 ↓)       각 "열(column)"별로 위→아래로 합침 → 1D(열 개수)
# 2D     1      옆 방향(열을 따라 →)         각 "행(row)"별로 좌→우로 합침 → 1D(행 개수)
# 3D     0      가장 바깥 차원(깊이/배치)     같은 (행,열) 위치를 "배치들" 간에 합침 → 2D(행×열)
# 3D     1      행 차원                    각 (배치,열)별로 행 방향으로 합침 → 2D(배치×열)
# 3D     2      열 차원                    각 (배치,행)별로 열 방향으로 합침 → 2D(배치×행)
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
print(np.sum([a, b], axis=0))
# [2 4 6]
print(np.sum([a, b], axis=1))
# [6 6]

## pandas-axis
# 대상         axis=0          axis=1          기본 동작
# ---------   -------------   -------------   --------------------------
# Series      index           (없음)           index 방향(위→아래)으로 집계
# DataFrame   index(행)       columns(열)      기본은 axis=0 (열 단위로 위→아래 집계)

print(price_df.head())
#              Open   High    Low  Close  Volume    Change
# Date
# 2013-07-25  26340  26440  26160  26300  169913       NaN
# 2013-07-26  26280  26380  25980  26060  272391 -0.009125
# 2013-07-29  25820  26000  25580  25660  236437 -0.015349
# 2013-07-30  25540  25900  25540  25800  188507  0.005456
# 2013-07-31  25600  25800  25580  25600  254710 -0.007752

print(price_df[['Open', 'High']].sum(axis=0))
# Open    36738858
# High    37089182
# dtype: int64
print(price_df[['Open', 'High']].sum(axis=1))
# Date
# 2013-07-25     52780
# 2013-07-26     52660
# 2013-07-29     51820
# 2013-07-30     51440
# 2013-07-31     51400
#                ...
# 2018-03-15    104020
# 2018-03-16    102640
# 2018-03-19    101960
# 2018-03-20    101900
# 2018-03-21    103560
# Length: 1142, dtype: int64

# DataFrame과 Series의 연산
# 기본적으로 Series의 index가 DataFrame의 column에 맞춰진다.
print((price_df - price_df.iloc[0]).head())
#              Open   High    Low  Close    Volume  Change
# Date
# 2013-07-25    0.0    0.0    0.0    0.0       0.0     NaN
# 2013-07-26  -60.0  -60.0 -180.0 -240.0  102478.0     NaN
# 2013-07-29 -520.0 -440.0 -580.0 -640.0   66524.0     NaN
# 2013-07-30 -800.0 -540.0 -620.0 -500.0   18594.0     NaN
# 2013-07-31 -740.0 -640.0 -580.0 -700.0   84797.0     NaN

# axis를 이용해 Series의 index와 DataFrame의 index를 맞춰서 연산할 수 있다.
close_series = price_df['Close']
print(price_df.sub(close_series, axis=0).head())
#             Open  High  Low  Close  Volume        Change
# Date
# 2013-07-25    40   140 -140      0  143613           NaN
# 2013-07-26   220   320  -80      0  246331 -26060.009125
# 2013-07-29   160   340  -80      0  210777 -25660.015349
# 2013-07-30  -260   100 -260      0  162707 -25799.994544
# 2013-07-31     0   200  -20      0  229110 -25600.007752
#             Change  Close  High  Low  Open  Volume

# DataFrame과 DataFrame의 연산
# index 및 column이 일치하는 element들만 서로 연산이 이뤄지고, 나머지는 nan
print((price_df - price_df[['Open', 'High']].iloc[:2]).head())
#             Change  Close  High  Low  Open  Volume
# Date
# 2013-07-25     NaN    NaN   0.0  NaN   0.0     NaN
# 2013-07-26     NaN    NaN   0.0  NaN   0.0     NaN
# 2013-07-29     NaN    NaN   NaN  NaN   NaN     NaN
# 2013-07-30     NaN    NaN   NaN  NaN   NaN     NaN
# 2013-07-31     NaN    NaN   NaN  NaN   NaN     NaN

