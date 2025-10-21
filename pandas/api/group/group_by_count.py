import numpy as np
import pandas as pd

df = pd.read_csv('../../../my_data/naver_finance/2016_12.csv')
df = df.dropna(subset=['PER(배)'])
# qcut
qcut = pd.qcut(df['PER(배)'], 3, labels=[1, 2, 3])
print(qcut)
# 0      2
# 1      3
# 2      1
# 3      3
# 4      3
#       ..
# 676    3
# 677    1
# 678    3
# 679    1
# 680    1
# Name: PER(배), Length: 669, dtype: category
# Categories (3, int64): [1 < 2 < 3]

df.loc[:, 'PER_Score2'] = pd.qcut(df['PER(배)'], 10, labels=range(1, 11))

print(df['PER_Score2'].isna().any())  # False
print(df['PER_Score2'].value_counts())
# PER_Score2
# 1     67
# 2     67
# 3     67
# 4     67
# 5     67
# 7     67
# 9     67
# 8     67
# 10    67
# 6     66
# Name: count, dtype: int64
