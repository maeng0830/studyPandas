import numpy as np
import pandas as pd
from numpy.ma.core import equal

print(np.nan == np.nan)  # False
print(5 < np.nan)  # False
print(5 > np.nan)  # False
print(5 == np.nan)  # False
print(5 != np.nan)  # True

####################################################

df1 = pd.DataFrame(
    {
        'a': [1, 2, 3],
        'b': [np.nan, 4, np.nan]
    }
)
print(df1)
#    a    b
# 0  1  NaN
# 1  2  4.0
# 2  3  NaN

print(df1['b'] == df1['b'])
# 0    False
# 1     True
# 2    False
# Name: b, dtype: bool

print(df1.ge(2))
#        a      b
# 0  False  False
# 1   True   True
# 2   True  False

print(df1.le(2))
#        a      b
# 0   True  False
# 1   True  False
# 2  False  False

# nan checking
finance_df = pd.read_csv('../../../my_data/naver_finance/2015_12.csv')
## For Series
print(finance_df['순이익률(%)'].hasnans)  # True
print(finance_df['순이익률(%)'].isna().any())  # True
print(finance_df['순이익률(%)'].isna().sum())  # 1

## For DataFrame
print(finance_df.isna().head())
#    ticker  매출액(억원)  영업이익률(%)  순이익률(%)  ...  PBR(배)  PSR(배)  price  price2
# 0   False    False     False    False  ...   False   False  False   False
# 1   False    False     False    False  ...   False   False  False   False
# 2   False    False     False    False  ...   False   False  False   False
# 3   False    False     False    False  ...   False   False  False   False
# 4   False    False     False    False  ...   False   False  False   False
print(finance_df.isna().any())
# ticker       False
# 매출액(억원)       True
# 영업이익률(%)      True
# 순이익률(%)       True
# 당기순이익(억원)     True
# ROE(%)        True
# ROA(%)        True
# ROIC(%)       True
# EPS(원)       False
# BPS(원)       False
# SPS(원)       False
# PER(배)        True
# PBR(배)       False
# PSR(배)        True
# price        False
# price2       False
# dtype: bool
print(finance_df.isna().any().any())  # True
print(finance_df.isna().any().all())  # False

## nan이 아닌 row만 추출
df2 = pd.DataFrame({
    'a': [1, 2, np.nan],
    'b': [np.nan, 5, 6]
})

print(df2['a'].notna() & df2['b'].notna())
# 0    False
# 1     True
# 2    False
# dtype: bool
print(df2[df2['a'].notna() & df2['b'].notna()])
#      a    b
# 1  2.0  5.0

print(df2.notna().all(axis=1))
# 0    False
# 1     True
# 2    False
# dtype: bool
print(df2[df2.notna().all(axis=1)])
#      a    b
# 1  2.0  5.0

## nan이 하나라도 있는 row는 제거
print(df2.dropna())
#      a    b
# 1  2.0  5.0
print(df2.dropna(subset=['a']))  # a 컬럼의 값이 nan인 row는 제거
#      a    b
# 0  1.0  NaN
# 1  2.0  5.0
print(df2.dropna(subset=['b']))  # b 컬럼의 값이 nan인 row는 제거
#      a    b
# 1  2.0  5.0
# 2  NaN  6.0