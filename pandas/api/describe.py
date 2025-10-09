import numpy as np
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv('../../my_data/naver_finance/2015_12.csv')
print(df.head())
#     ticker      매출액(억원)  영업이익률(%)  ...   PSR(배)     price    price2
# 0    AK홀딩스   28071.4790     3.787  ...  0.29825   63200.0   56000.0
# 1      BGF   43342.8000     4.236  ...  1.00711   44202.0   42140.0
# 2  BNK금융지주   51740.2540    13.455  ...  0.42635    8420.0    8680.0
# 3      BYC    1821.9598    11.598  ...  2.11849  459500.0  397000.0
# 4       CJ  211667.0800     5.789  ...  0.39808  236684.0  176334.0

# metadata
print(df.shape)
# (681, 16)
print(df.dtypes)
# ticker        object
# 매출액(억원)      float64
# 영업이익률(%)     float64
# 순이익률(%)      float64
# 당기순이익(억원)    float64
# ROE(%)       float64
# ROA(%)       float64
# ROIC(%)      float64
# EPS(원)       float64
# BPS(원)       float64
# SPS(원)       float64
# PER(배)       float64
# PBR(배)       float64
# PSR(배)       float64
# price        float64
# price2       float64
# dtype: object

print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 681 entries, 0 to 680
# Data columns (total 16 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   ticker     681 non-null    object
#  1   매출액(억원)    680 non-null    float64
#  2   영업이익률(%)   680 non-null    float64
#  3   순이익률(%)    680 non-null    float64
#  4   당기순이익(억원)  680 non-null    float64
#  5   ROE(%)     665 non-null    float64
#  6   ROA(%)     665 non-null    float64
#  7   ROIC(%)    611 non-null    float64
#  8   EPS(원)     681 non-null    float64
#  9   BPS(원)     681 non-null    float64
#  10  SPS(원)     681 non-null    float64
#  11  PER(배)     668 non-null    float64
#  12  PBR(배)     681 non-null    float64
#  13  PSR(배)     668 non-null    float64
#  14  price      681 non-null    float64
#  15  price2     681 non-null    float64
# dtypes: float64(15), object(1)
# memory usage: 85.3+ KB
# None

##############################################################
# describe()으로 기초 통계값을 산출 할 때는, float, integer 와 같은 산술 통계가 가능한 dtype의 series에 대해서만 동작한다.
# 이것은 df.describe(include=[np.number])가 디폴트로 적용되어 있기 때문이다.
print(df.describe())
#          매출액(억원)  영업이익률(%)  순이익률(%)  ...  PSR(배)      price     price2
# count     680.00    680.00   680.00  ...  668.00     681.00     681.00
# mean    30112.80      3.88     7.67  ...    1.92   47344.20   41784.56
# std    108134.17     13.14   151.57  ...   19.85  117063.70   96318.57
# min         3.56   -191.60  -193.43  ...    0.01     158.00     154.00
# 25%      1727.09      1.53     0.37  ...    0.31    3903.00    4060.00
# 50%      4692.06      4.19     3.07  ...    0.59   12018.00   10900.00
# 75%     15243.67      8.31     6.61  ...    1.14   40496.00   39750.00
# max   2006534.90     64.27  3923.34  ...  511.72 1225000.00 1064000.00
# [8 rows x 15 columns]
print(df.describe().T)
#            count     mean       std  ...      50%      75%        max
# 매출액(억원)   680.00 30112.80 108134.17  ...  4692.06 15243.67 2006534.90
# 영업이익률(%)  680.00     3.88     13.14  ...     4.19     8.31      64.27
# 순이익률(%)   680.00     7.67    151.57  ...     3.07     6.61    3923.34
# 당기순이익(억원) 680.00  1312.76  10133.60  ...   118.92   504.20  190601.44
# ROE(%)    665.00     4.51    130.08  ...     5.35     9.77    3122.57
# ROA(%)    665.00     1.84      9.51  ...     2.31     5.34      60.29
# ROIC(%)   611.00    -3.01    195.16  ...     5.21    10.55     271.96
# EPS(원)    681.00   426.08  34193.00  ...   539.11  2197.65   93713.01
# BPS(원)    681.00 47451.88 152959.28  ... 10988.99 39550.23 3017474.00
# SPS(원)    681.00 95471.75 316794.46  ... 22559.92 72356.34 5553036.50
# PER(배)    668.00    18.92    134.92  ...    11.74    24.06    2808.26
# PBR(배)    681.00     1.58      2.04  ...     0.96     1.67      21.15
# PSR(배)    668.00     1.92     19.85  ...     0.59     1.14     511.72
# price     681.00 47344.20 117063.70  ... 12018.00 40496.00 1225000.00
# price2    681.00 41784.56  96318.57  ... 10900.00 39750.00 1064000.00
# [15 rows x 8 columns]

# Categorized 가능한 string과 같은 dtype의 series에 대해서도 describe이 가능하다.
print(df.describe(include=[pd.Categorical]).T)
#        count unique    top freq
# ticker   681    681  AK홀딩스    1