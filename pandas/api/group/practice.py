import numpy as np
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)
a_df = pd.read_csv('../../../my_data/Small_and_Big.csv', index_col=[0])
print(a_df.head(2))
#          date  종목명  PBR(IFRS-연결)  베타 (M,5Yr)  수익률(%)  시가총액 (보통)(평균)(원)
# 0  2000-07-31  BYC          0.21     0.47940   -0.58      2.778600e+10
# 1  2000-07-31   CJ          0.51     1.16611   -9.00      1.160889e+12

median_df = a_df.groupby(['date']).agg({'시가총액 (보통)(평균)(원)': ['median']})
median_df.rename(columns={'시가총액 (보통)(평균)(원)': '시가총액'}, inplace=True)  # inplace=True는 새로운 df를 반환하지 않고 기존 객체를 변경
median_df.columns = median_df.columns.get_level_values(0) + '_' + median_df.columns.get_level_values(1)
print(median_df.head(2))
#               시가총액_median
# date
# 2000-07-31 34947000000.00
# 2000-08-31 33684000000.00

###################################################################
a_df['big_or_small'] = a_df['시가총액 (보통)(평균)(원)'] >= median_df['시가총액_median'].reindex(a_df['date']).values
a_df.loc[a_df['big_or_small'], 'big_or_small'] = '대형주'
a_df.loc[a_df['big_or_small'] == False, 'big_or_small'] = '소형주'
print(a_df.head(2))
