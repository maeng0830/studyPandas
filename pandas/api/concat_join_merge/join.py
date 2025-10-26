import numpy as np
import pandas as pd
import FinanceDataReader as fdr

pd.set_option('display.float_format', lambda x: '%.2f' % x)

samsung_df = fdr.DataReader('005390', '2009-01-01', '2017-12-31')
kodex_df = fdr.DataReader('069500', '2009-01-01', '2017-12-31')


# join은 index 또는 columns를 기준으로 두 개의 DF를 합칠 떄 사용한다.
# concat과의 차이라면, concat은 index 또는 column의 이름을 기준으로 합치지만, join은 value를 기준으로 합친다.
left = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2'],
        'B': ['B0', 'B1', 'B2'],
    },
    index=['K0', 'K1', 'K2']
)

right = pd.DataFrame(
    {
        'C': ['C0', 'C1', 'C2'],
        'D': ['D0', 'D1', 'D2'],

    }, index=['K0', 'K2', 'K3']
)

print(left.join(right))  # default -> index join, left join
#      A   B    C    D
# K0  A0  B0   C0   D0
# K1  A1  B1  NaN  NaN
# K2  A2  B2   C1   D1

print(left.join(right, how='right'))
#       A    B   C   D
# K0   A0   B0  C0  D0
# K2   A2   B2  C1  D1
# K3  NaN  NaN  C2  D2

print(left.join(right, how='outer'))
#       A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C1   D1
# K3  NaN  NaN   C2   D2

print(left.join(right, how='inner'))
#      A   B   C   D
# K0  A0  B0  C0  D0
# K2  A2  B2  C1  D1

## on은 join 기준이 되는 calling-df의 columns를 값으로 가지며, 해당 columns와 called-df의 index를 기준으로 join 된다.
left = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
        'key': ['K0', 'K1', 'K0', 'K1']
    }
)

right = pd.DataFrame(
    {
        'C': ['C0', 'C1'],
        'D': ['D0', 'D1'],
    },
    index=['K0', 'K1']
)

print(left.join(right, on='key'))
#     A   B key   C   D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K0  C0  D0
# 3  A3  B3  K1  C1  D1

print(left.set_index('key').join(right))
#       A   B   C   D
# key
# K0   A0  B0  C0  D0
# K1   A1  B1  C1  D1
# K0   A2  B2  C0  D0
# K1   A3  B3  C1  D1

## l_suffix, r_suffix
a = pd.DataFrame([1, 2, 3], index=['a', 'b', 'c'], columns=['안녕'])
b = pd.DataFrame([4, 2, 6], index=['a', 'b', 'd'], columns=['안녕'])

print(a.join(b, lsuffix="_x", rsuffix="_y", how='inner'))
#    안녕_x  안녕_y
# a     1     4
# b     2     2

