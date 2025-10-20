import numpy as np
import pandas as pd

df = pd.read_csv('../../../my_data/naver_finance/2016_12.csv')

# boolean indexing & loc
bound1 = df['PER(배)'] >= 10
bound2 = (5 <= df['PER(배)']) & (df['PER(배)'] < 10)
bound3 = (0 <= df['PER(배)']) & (df['PER(배)'] < 5)
bound4 = df['PER(배)'] < 0

## set operation
df.loc[bound1, 'PER_Score'] = 1
df.loc[bound2, 'PER_Score'] = 2
df.loc[bound3, 'PER_Score'] = 3
df.loc[bound4, 'PER_Score'] = -1

print(df['PER_Score'].isna().any())
# True
print(df['PER_Score'].head())
# 0    1.0
# 1    1.0
# 2    2.0
# 3    1.0
# 4    1.0
# Name: PER_Score, dtype: float64

print(df['PER_Score'].nunique())
# 4

print(df['PER_Score'].value_counts())
# PER_Score
#  1.0    378
#  2.0    148
# -1.0    120
#  3.0     23
# Name: count, dtype: int64

###############################################
# boolean series
df.loc[:, 'PER_Score1'] = bound1 * 1 + bound2 * 2 + bound3 * 3 + bound4 * -1

print(df['PER_Score1'].isna().any())
# False
print(df['PER_Score1'].head())
# 0    1
# 1    1
# 2    2
# 3    1
# 4    1
# Name: PER_Score1, dtype: int64

print(df['PER_Score1'].nunique())
# 5

print(df['PER_Score1'].value_counts())
# PER_Score1
#  1    378
#  2    148
# -1    120
#  3     23
#  0     12
# Name: count, dtype: int64

####################################################
# cut()
per_cuts = pd.cut(
    df['PER(배)'],
    [-np.inf, 0, 5, 10, np.inf],
)

print(per_cuts.head())
# 0    (10.0, inf]
# 1    (10.0, inf]
# 2    (5.0, 10.0]
# 3    (10.0, inf]
# 4    (10.0, inf]
# Name: PER(배), dtype: category
# Categories (4, interval[float64, right]): [(-inf, 0.0] < (0.0, 5.0] < (5.0, 10.0] < (10.0, inf]]

print(per_cuts.value_counts())
# PER(배)
# (10.0, inf]    378
# (5.0, 10.0]    148
# (-inf, 0.0]    120
# (0.0, 5.0]      23
# Name: count, dtype: int64

bins = [-np.inf, 10, 20, np.inf]
labels = ['저평가주', '보통주', '고평가주']

per_cuts2 = pd.cut(
    df['PER(배)'],
    bins=bins,
    labels=labels,
)

print(per_cuts2.head())
# 0     보통주
# 1    고평가주
# 2    저평가주
# 3     보통주
# 4    고평가주
# Name: PER(배), dtype: category
# Categories (3, object): ['저평가주' < '보통주' < '고평가주']