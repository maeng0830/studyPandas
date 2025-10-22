import numpy as np
import pandas as pd

df = pd.read_csv('../../../my_data/naver_finance/2016_12.csv')
df = df.dropna()
print(df.shape)
# (609, 17)

g_df = df.copy()
g_df['rtn'] = g_df['price2'] / g_df['price'] - 1
g_df.loc[:, 'PER_Score'] = pd.qcut(df['PER(배)'], 10, labels=range(1, 11))
g_df.loc[:, 'PBR_Score'] = pd.qcut(df['PBR(배)'], 10, labels=range(1, 11))
g_df.set_index('ticker', inplace=True)

# groupby()는 실제로 grouping은 하지 않고, grouping이 가능한지 validation만 진행한다.
# aggregation은 aggregating column + aggregation function
# grouping은 grouping column + aggregating column + aggregating function

##########################################################################################
# groupby

print(g_df.groupby('PER_Score'))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001EF011417C0>
print(g_df.groupby(['PBR_Score', 'PER_Score']))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001EF011417C0>

g_df_obj = g_df.groupby(['PBR_Score', 'PER_Score'])
print(g_df_obj.ngroups)
# 96

print(g_df_obj.size())
# PBR_Score  PER_Score
# 1          1             5
#            2            11
#            3            11
#            4            11
#            5             7
#                         ..
# 10         6             1
#            7             2
#            8            15
#            9            11
#            10           14
# Length: 100, dtype: int64
print(g_df_obj.size().loc[1])
# PER_Score
# 1      5
# 2     11
# 3     11
# 4     11
# 5      7
# 6      2
# 7      4
# 8      0
# 9      3
# 10     7
# dtype: int64
print(g_df_obj.size().loc[1][1])
# 5

print(type(g_df_obj.groups))
# <class 'pandas.io.formats.printing.PrettyDict'>
print(g_df_obj.groups.keys())
# dict_keys([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 9), (1, 10), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (9, 1), (9, 2), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (10, 1), (10, 2), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)])

############################################################################################
# aggregation
pbr_rtn_df = g_df.groupby('PBR_Score').agg({'rtn': 'mean'})
per_rtn_df = g_df.groupby('PER_Score').agg({'rtn': 'mean'})  # == g_df.groupby('PER_Score')['rtn'].agg('mean').head(2)

print(pbr_rtn_df)
#                 rtn
# PBR_Score
# 1         -0.001363
# 2          0.020453
# 3         -0.020788
# 4          0.160985
# 5         -0.011614
# 6         -0.043329
# 7          0.150012
# 8          0.057876
# 9          0.139403
# 10         0.053526
print(per_rtn_df)
#                 rtn
# PER_Score
# 1         -0.061915
# 2         -0.083212
# 3         -0.037584
# 4          0.056213
# 5          0.000077
# 6          0.095373
# 7          0.150638
# 8          0.144230
# 9          0.047995
# 10         0.195620


print(g_df.groupby('PER_Score')[['rtn', 'PBR(배)']].agg('mean').head(2))
#                 rtn    PBR(배)
# PER_Score
# 1         -0.061915  1.838688
# 2         -0.083212  1.323324
print(g_df.groupby('PER_Score')[['rtn', 'PBR(배)']].agg(['mean', 'std']).head(2))
#                 rtn              PBR(배)
#                mean       std      mean       std
# PER_Score
# 1         -0.061915  0.327539  1.838688  2.214702
# 2         -0.083212  0.780563  1.323324  1.167421
print(
    g_df.groupby('PER_Score').agg(
        {
            'rtn': ['mean', 'std'],
            'PBR(배)': ['min']
        }
    )
)
#                 rtn             PBR(배)
#                mean       std      min
# PER_Score
# 1         -0.061915  0.327539  0.21022
# 2         -0.083212  0.780563 -0.23757
# 3         -0.037584  0.285682  0.24983
# 4          0.056213  0.308327  0.29320
# 5          0.000077  0.206081  0.29196
# 6          0.095373  0.402752  0.43369
# 7          0.150638  0.648031  0.36033
# 8          0.144230  0.545007  0.46555
# 9          0.047995  0.477527  0.33169
# 10         0.195620  0.478981  0.28654